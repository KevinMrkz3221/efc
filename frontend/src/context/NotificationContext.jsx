import React, { createContext, useState, useContext } from 'react';

const NotificationContext = createContext();

export function useNotification() {
  return useContext(NotificationContext);
}

export function NotificationProvider({ children }) {
  const [message, setMessage] = useState('');
  const [type, setType] = useState('info'); // 'info', 'error', 'success'

  const showMessage = (msg, msgType = 'info') => {
    setMessage(msg);
    setType(msgType);
    setTimeout(() => setMessage(''), 3000);
  };

  return (
    <NotificationContext.Provider value={{ showMessage }}>
      {children}
      {message && (
        <div style={{
          position: 'fixed',
          top: 20,
          left: '50%',
          transform: 'translateX(-50%)',
          background: type === 'error' ? '#f44336' : type === 'success' ? '#4caf50' : '#2196f3',
          color: '#fff',
          padding: '1rem 2rem',
          borderRadius: 8,
          zIndex: 9999,
          boxShadow: '0 2px 8px rgba(0,0,0,0.2)'
        }}>
          {message}
        </div>
      )}
    </NotificationContext.Provider>
  );
}
