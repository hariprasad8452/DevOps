const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors()); // Allows the frontend to talk to the backend

app.get('/api/data', (req, res) => {
    res.json({ message: "Hello from the Kubernetes Backend!", status: "Connected" });
});

app.listen(5000, () => console.log('Backend running on port 5000'));
