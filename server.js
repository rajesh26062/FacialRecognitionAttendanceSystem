const http = require('http');
const { exec } = require('child_process');
const path = require('path');

const server = http.createServer((req, res) => {
    if (req.method === 'POST' && req.url === '/run') {
        // Specify the full path to your Python script
        const pythonScriptPath = path.join(__dirname, 'login.py'); // Adjust the path as needed

        exec(`python ${pythonScriptPath}`, (error, stdout, stderr) => {
            if (error) {
                console.error(`Error: ${error}`);
                res.statusCode = 500;
                res.end(`Error: ${error}`);
            } else {
                console.log(`Output: ${stdout}`);
                res.statusCode = 200;
                res.end(`Output: ${stdout}`);
            }
        });
    } else {
        res.statusCode = 404;
        res.end('Not Found');
    }
});

const port = 8081; // Choose a port number
server.listen(port, () => {
    console.log(`Server is listening on port ${port}`);
});
