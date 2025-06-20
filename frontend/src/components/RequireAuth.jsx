import React from 'react';
import { Navigate } from 'react-router-dom';

// Esta función verifica si el usuario está autenticado (por ejemplo, si hay un token en localStorage)
function isAuthenticated() {
  return !!localStorage.getItem('access');
}

export default function RequireAuth({ children }) {
  if (!isAuthenticated()) {
    return <Navigate to="/login" replace />;
  }
  return children;
}
