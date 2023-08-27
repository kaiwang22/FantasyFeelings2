import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';
import Chart from "chart.js/auto";
import { CategoryScale } from "chart.js";
import './styles/sentimentgraph.css'

function SentimentGraph({ player_id }) {
  const [sentimentEntries, setSentimentEntries] = useState([]);
  Chart.register(CategoryScale);

  useEffect(() => {
    // Fetch sentiment entries for the given player ID
    axios.get(`http://127.0.0.1:8000/api/players/${player_id}/sentiment/`)
      .then(response => {
        setSentimentEntries(response.data);
      })
      .catch(error => {
        console.error('Error fetching sentiment entries:', error);
      });
  }, []); // Empty dependency array to fetch data only once

  const dates = sentimentEntries.map(entry => {
    const parsedDate = new Date(entry.times);
    return parsedDate;
  });
  dates.sort((a, b) => a - b);
  const formattedDates = dates.map(date => date.toLocaleDateString());
  const scores = sentimentEntries.map(entry => entry.score);
  const titles = sentimentEntries.map(entry => entry.title);

  const data = {
    labels: formattedDates,
    datasets: [
      {
        label: 'Sentiment Score',
        data: scores,
        fill: false,
        borderColor: 'blue',
      },
    ],
  };

  // Set options for the chart
  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      tooltip: {
        callbacks: {
          title: function (context) {
            const index = context[0].dataIndex;
            return titles[index]; // Show the title for the hovered point
          },
        },
      },
    },
  };

  return (
    <div className="chart-container">
      <h2>Sentiment Graph</h2>
      <Line data={data} options={options} />
    </div>
  );
}

export default SentimentGraph;


