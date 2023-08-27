import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';
import SentimentGraph from './sentimentgraph';
import SearchBar from './searchbar'



function PlayerDetail({ match }) {
  const [playerDetails, setPlayerDetails] = useState({});
  const { player_id: initialPlayerId }= useParams();
  const [player_id, setPlayerId] = useState(initialPlayerId);
  const navigate = useNavigate();

  useEffect(() => { 

    // Fetch player details
    axios.get(`http://127.0.0.1:8000/api/players/${player_id}/`).then((response) => {
      setPlayerDetails(response.data);
  })
      .catch((error) => {
        console.error('Error fetching player details:', error);
        setPlayerDetails({});
    });

  }, [player_id]);

  const handlePlayerSearch = (newPlayerId) => {
    setPlayerId(newPlayerId);
  };

  return (
    <div>
    <button onClick={() => navigate('/')}>Home</button>
    <SearchBar onPlayerSearch={handlePlayerSearch}/>
      <h1>{playerDetails.name}</h1>
      <p>Position: {playerDetails.position}</p>
      <p>Team: {playerDetails.team}</p>
      <p>Current Feeling: {playerDetails.current_feeling}</p>
      <SentimentGraph player_id={player_id} key={player_id} />
   
    </div>
  );
}

export default PlayerDetail;
