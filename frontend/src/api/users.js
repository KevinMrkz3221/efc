const API_URL = import.meta.env.VITE_EFC_API_URL;

export async function fetchUsers(token) {
  let res = await fetch(`${API_URL}/api/v1/user/users/`, {
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json',
    },
  });
  if (res.status === 401) throw new Error('SESSION_EXPIRED');
  if (!res.ok) throw new Error('No autorizado o error en la petición');
  return res.json();
}

export async function createUser(token, userData) {
  const res = await fetch(`${API_URL}/api/v1/user/users/`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(userData),
  });
  if (res.status === 401) throw new Error('SESSION_EXPIRED');
  if (!res.ok) throw new Error('Error al crear usuario');
  return res.json();
}

export async function updateUser(token, id, userData) {
  const res = await fetch(`${API_URL}/api/v1/user/users/${id}/`, {
    method: 'PUT',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(userData),
  });
  if (res.status === 401) throw new Error('SESSION_EXPIRED');
  if (!res.ok) throw new Error('Error al actualizar usuario');
  return res.json();
}

export async function deleteUser(token, id) {
  const res = await fetch(`${API_URL}/api/v1/user/users/${id}/`, {
    method: 'DELETE',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json',
    },
  });
  if (res.status === 401) throw new Error('SESSION_EXPIRED');
  if (!res.ok) throw new Error('Error al eliminar usuario');
  return true;
}
