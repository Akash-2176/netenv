import React from "react";

function SessionTable({ sessions }) {
  return (
    <table className="table-auto w-full">
      <thead>
        <tr>
          <th>S.No</th>
          <th>Session Key</th>
          <th>Source IP</th>
          <th>Destination IP</th>
          <th>Protocol</th>
          <th>Source Port</th>
          <th>Destination Port</th>
          <th>Packet Count</th>
          <th>Total Volume (bytes)</th>
        </tr>
      </thead>
      <tbody>
        {sessions.map((session, index) => (
          <tr key={session.session_key}>
            <td>{index + 1}</td>
            <td>{session.session_key}</td>
            <td>{session.src_ip}</td>
            <td>{session.dst_ip}</td>
            <td>{session.protocol}</td>
            <td>{session.src_port}</td>
            <td>{session.dst_port}</td>
            <td>{session.packet_count}</td>
            <td>{session.total_volume}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default SessionTable;
