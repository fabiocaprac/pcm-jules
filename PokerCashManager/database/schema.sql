-- Enable pgcrypto extension for gen_random_uuid()
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Table for Organizers (Implicitly needed)
CREATE TABLE organizers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW() -- Added updated_at for consistency
);

-- Table for Cash Boxes
CREATE TABLE cash_boxes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    active_session_id UUID REFERENCES sessions(id) ON DELETE SET NULL, -- Foreign key, initially NULL or set later
    organizer_id UUID NOT NULL REFERENCES organizers(id),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Table for Sessions
CREATE TABLE sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    cash_box_id UUID NOT NULL REFERENCES cash_boxes(id),
    name TEXT NOT NULL,
    started_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    ended_at TIMESTAMPTZ,
    status TEXT NOT NULL DEFAULT 'Ativa', -- e.g., 'Ativa', 'Finalizada'
    created_by_organizer_id UUID NOT NULL REFERENCES organizers(id),
    finalized_by_organizer_id UUID REFERENCES organizers(id),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Now that sessions table is defined, we can alter cash_boxes to add the foreign key constraint
-- This avoids a circular dependency if active_session_id was NOT NULL and referenced immediately.
-- However, since active_session_id IS NULLABLE, this step is not strictly necessary for table creation order.
-- But it's good practice to be mindful of such dependencies.
-- ALTER TABLE cash_boxes ADD CONSTRAINT fk_active_session FOREIGN KEY (active_session_id) REFERENCES sessions(id) ON DELETE SET NULL;
-- For this schema, direct definition in cash_boxes is fine as active_session_id is nullable.

-- Table for Player Profiles
CREATE TABLE player_profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    full_name TEXT NOT NULL,
    nickname TEXT,
    whatsapp_contact TEXT,
    pix_key TEXT,
    credit_limit DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    global_balance DECIMAL(10, 2) NOT NULL DEFAULT 0.00, -- SaldoGlobalAcumulado
    registered_by_organizer_id UUID NOT NULL REFERENCES organizers(id),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Table for Players in Session
CREATE TABLE players_in_session (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,
    player_profile_id UUID NOT NULL REFERENCES player_profiles(id) ON DELETE RESTRICT,
    display_name TEXT NOT NULL, -- NomeJogadorExibicao
    session_buy_ins_total DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    session_cashouts_total DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    session_payments_total DECIMAL(10, 2) NOT NULL DEFAULT 0.00, -- Can be negative
    session_pending_balance DECIMAL(10, 2) NOT NULL DEFAULT 0.00, -- SaldoPendenteSessao
    current_chips_balance DECIMAL(10, 2) NOT NULL DEFAULT 0.00, -- SaldoAtualEmJogo
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE (session_id, player_profile_id) -- A player can only be in a session once
);

-- Table for Transactions
CREATE TABLE transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,
    player_in_session_id UUID NOT NULL REFERENCES players_in_session(id) ON DELETE CASCADE,
    transaction_type TEXT NOT NULL, -- "BuyIn", "Cashout", "Pagamento"
    amount DECIMAL(10, 2) NOT NULL,
    payment_method TEXT NOT NULL, -- "Dinheiro", "PIX", "CartaoCredito", "CartaoDebito", "Nenhum/Pendente"
    payment_status TEXT NOT NULL, -- "Pago", "Pendente"
    payment_direction TEXT, -- "EntradaCaixa", "SaidaCaixa" (relevant for "Pagamento")
    transaction_time TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    executed_by_organizer_id UUID NOT NULL REFERENCES organizers(id),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Table for Chip Definitions
CREATE TABLE chip_definitions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,
    value DECIMAL(10, 2) NOT NULL,
    color TEXT,
    initial_quantity INTEGER NOT NULL DEFAULT 0,
    current_quantity INTEGER,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE (session_id, value) -- Avoid duplicate chip values per session
);

-- Table for Activity Logs
CREATE TABLE activity_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_time TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    event_type TEXT NOT NULL, -- "CriacaoSessao", "AddJogador", etc.
    description TEXT NOT NULL,
    responsible_organizer_id UUID NOT NULL REFERENCES organizers(id),
    session_id UUID REFERENCES sessions(id) ON DELETE SET NULL,
    transaction_id UUID REFERENCES transactions(id) ON DELETE SET NULL,
    player_in_session_id UUID REFERENCES players_in_session(id) ON DELETE SET NULL,
    player_name_log TEXT, -- NomeJogadorLog
    logged_value DECIMAL(10, 2),
    additional_details JSONB, -- Using JSONB for structured details
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Note: Triggers for automatically updating `updated_at` columns are not included here
-- but are recommended for a production environment.
-- Example for one table:
-- CREATE OR REPLACE FUNCTION update_updated_at_column()
-- RETURNS TRIGGER AS $$
-- BEGIN
--    NEW.updated_at = NOW();
--    RETURN NEW;
-- END;
-- $$ language 'plpgsql';
--
-- CREATE TRIGGER update_organizers_updated_at
-- BEFORE UPDATE ON organizers
-- FOR EACH ROW
-- EXECUTE FUNCTION update_updated_at_column();
-- (Repeat for other tables)
