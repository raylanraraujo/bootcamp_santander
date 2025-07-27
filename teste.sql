CREATE TABLE reservas (
    id INT,
    id_usuario INT,
    id_destino INT,
    data DATE,
    status VARCHAR(255) DEFAUlT 'pendente'
);