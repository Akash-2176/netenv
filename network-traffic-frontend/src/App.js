import React from "react";
import Dashboard from "./components/Dashboard";

function App() {
  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <h1 className="text-3xl font-bold text-center text-blue-600 mb-8">
        Network Traffic Dashboard
      </h1>
      <Dashboard />
    </div>
  );
}

export default App;
