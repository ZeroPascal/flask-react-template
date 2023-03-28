import React from 'react';
import { useSelector } from 'react-redux';

import './App.css';
import Socket from './app/Socket/Socket';
import { socket_connected } from './app/Socket/socketSelectors';
import { RootState } from './app/store';
import MainPage from './Components/Pages/MainPage';

function App() {
  const state = useSelector((state: RootState) => state)
  return (
    <div className="App">
     <Socket/>
     {socket_connected(state)?<MainPage/>:'Socket Not Connected'}
    </div>
  );
}

export default App;
