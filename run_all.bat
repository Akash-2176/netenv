@echo off

echo Starting packet capture...
start cmd /k "cd backend && python packet_cap.py"

echo Starting server API...
start cmd /k "cd backend && python server-api.py"

echo Starting frontend...
start cmd /k "cd network-traffic-frontend && npm run start"

echo All services started successfully.
