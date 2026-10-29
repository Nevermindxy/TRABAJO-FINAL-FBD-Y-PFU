CREATE DATABASE IF NOT EXISTS proyecto_integrador;
USE proyecto_integrador;

CREATE TABLE IF NOT EXISTS datos_formulario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    mensaje TEXT,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);