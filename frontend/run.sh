#!/bin/sh

echo "frontend trying to connect to backend"

curl -s http://backend:5000 || echo "failed to connect to backend"
