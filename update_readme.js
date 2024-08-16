const fs = require('fs');
const readline = require('readline');

const startMarker = '<!-- START_QUOTES -->';
const endMarker = '<!-- END_QUOTES -->';

const rl = readline.createInterface({
    input: fs.createReadStream('alintilar.txt'),
    output: process.stdout,
    terminal: false
});

rl.on('line', (line) => {
    fs.readFile('readme.md', 'utf8', (err, data) => {
        if (err) throw err;

        const startIndex = data.indexOf(startMarker);
        const endIndex = data.indexOf(endMarker);

        if (startIndex === -1 || endIndex === -1 || startIndex >= endIndex) {
            console.error('Markers not found or in wrong order.');
            return;
        }

        const beforeQuotes = data.substring(0, startIndex + startMarker.length);
        const afterQuotes = data.substring(endIndex);

        const newContent = `${beforeQuotes}\n> ${line}\n${afterQuotes}`;

        fs.writeFile('readme.md', newContent, 'utf8', (err) => {
            if (err) throw err;
            console.log('Alıntı eklendi:', line);
        });
    });
});
