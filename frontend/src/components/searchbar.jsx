import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom'; 

function SearchBar() {
  const [searchInput, setSearchInput] = useState('');
  const [playerExists, setPlayerExists] = useState(false);
  const navigate = useNavigate(); 

  const searchForPlayer = async (playerName) => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/api/players/search/?search=${playerName}`);
      return response.data[0]?.id; 
    } catch (error) {
      console.error('Error searching for player:', error);
      return null;
    }
  };

  const handleSearchSubmit = async (event) => {
    event.preventDefault();
    const player_id = await searchForPlayer(searchInput);

    if (player_id) {
        navigate(`/player/${player_id}`);
      } else {
        setPlayerExists(false);
      }
    };

  return (
<form onSubmit={handleSearchSubmit}>
        <input
          type="text"
          placeholder="Search for a player..."
          value={searchInput}
          onChange={(event) => setSearchInput(event.target.value)}
        />
        <button type="submit">Search</button>
      </form>
  );
}

export default SearchBar