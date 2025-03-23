const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const PORT = 5000;


// Middleware
app.use(bodyParser.json());


// Mock user authentication
const users = [
  { matricNumber: '12345', email: 'parent1@example.com' },
  { matricNumber: '67890', email: 'parent2@example.com' },
];

// Endpoint to handle form submission

document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('submittion')
})
app.post('/submit-exeat', (req, res) => {
  const { matricNumber, email, reason } = req.body;

  // Validate user
  const user = users.find(
    (u) => u.matricNumber === matricNumber && u.email === email
  );

  if (!user) {
    return res.status(401).json({ message: 'Authentication failed' });
  }

  // Process the exeat request
  console.log('Exeat Request:', { matricNumber, email, reason });
  res.status(200).json({ message: 'Exeat request submitted successfully' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});