import React, { useState, useEffect } from "react";
import axios from "axios";
import SessionTable from "./SessionTable";

function Dashboard() {
  const [sessions, setSessions] = useState([]);

  useEffect(() => {
    // Function to fetch session data
    const fetchSessions = () => {
      axios
        .get("http://localhost:5000/api/sessions")
        .then((response) => {
          setSessions(response.data);
        })
        .catch((error) => {
          console.error("Error fetching session data:", error);
        });
    };

    // Fetch data initially and set interval
    fetchSessions();
    const intervalId = setInterval(fetchSessions, 3000);

    // Cleanup interval on component unmount
    return () => clearInterval(intervalId);
  }, []);

  return (
    <div className="container mx-auto">
      <SessionTable sessions={sessions} />
    </div>
  );
}

export default Dashboard;
