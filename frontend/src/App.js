import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LandingPage from './components/landingpage';
import PlayerDetail from './components/playerdetail';


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage/>} />
        <Route path="/player/:player_id" element={<PlayerDetail/>} />
      </Routes>
    </Router>
  );
}

export default App;
