import React, { useEffect } from 'react';
import io from 'socket.io-client';

export default function Message() {
    const socket = io('http://localhost:5000');
    return (
        <div>
            <h1>Hi! Message page.</h1>
        </div>
    ); 
}