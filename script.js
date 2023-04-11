let newsletterLink = null;

document.getElementById('email').addEventListener('keypress', async function (event) {
    if (event.key === 'Enter') {
        const email = this.value;
        const url = `http://localhost:8080/?email=${encodeURIComponent(email)}`;

        // Clear table content
        document.getElementById('result').innerHTML = '';

        // Show loading element
        document.getElementById('loading').classList.remove('hidden');
        // Hide table header
        document.getElementById('result-table').querySelector('thead').classList.add('hidden');

        // Remove newsletter link if it exists
        if (newsletterLink) {
            newsletterLink.remove();
            newsletterLink = null;
        }

        try {
            const response = await fetch(url);
            const result = await response.json();
            displayResults(result);
        } catch (error) {
            console.error('Error fetching data:', error);
            document.getElementById('result').textContent = 'Error: Unable to fetch data.';
        } finally {
            // Hide loading element
            document.getElementById('loading').classList.add('hidden');
        }
    }
});

function displayResults(data) {
    const resultTable = document.getElementById('result');
    resultTable.innerHTML = '';

    for (const category in data) {
        if (category === 'profiles') {
            for (const platform in data[category]) {
                const row = document.createElement('tr');
                const platformCell = document.createElement('td');
                platformCell.textContent = platform;
                row.appendChild(platformCell);

                const resultCell = document.createElement('td');
                const icon = document.createElement('img');
                icon.width = 16;
                icon.height = 16;

                if (data[category][platform] === 'true') {
                    icon.src = './img/true.png';
                } else if (data[category][platform] === 'unknown') {
                    icon.src = './img/unknown.png';
                } else {
                    icon.src = './img/false.png';
                }

                resultCell.appendChild(icon);
                row.appendChild(resultCell);

                resultTable.appendChild(row);
            }
        } else {
            const row = document.createElement('tr');
            const platformCell = document.createElement('td');
            platformCell.textContent = category;
            row.appendChild(platformCell);

            const resultCell = document.createElement('td');
            if (category === 'Name') {
                if (data[category] === 'N/A') {
                    const icon = document.createElement('img');
                    icon.width = 16;
                    icon.height = 16;
                    icon.src = './img/false.png';
                    resultCell.appendChild(icon);
                } else {
                    resultCell.textContent = data[category];
                }
            } else if (category === 'Photo') {
                const icon = document.createElement('img');
                if (data[category] === 'N/A') {
                    icon.width = 16;
                    icon.height = 16;
                    icon.src = './img/false.png';
                } else {
                    icon.width = 64;
                    icon.height = 64;
                    icon.src = data[category];
                }
                resultCell.appendChild(icon);
            } else {
                const icon = document.createElement('img');
                icon.width = 16;
                icon.height = 16;

                if (data[category] === 'true') {
                    icon.src = './img/true.png';
                } else if (data[category] === 'unknown') {
                    icon.src = './img/unknown.png';
                } else {
                    icon.src = './img/false.png';
                }

                resultCell.appendChild(icon);
            }

            row.appendChild(resultCell);
            resultTable.appendChild(row);
        }
    }

    // Show table header
    document.getElementById('result-table').querySelector('thead').classList.remove('hidden');

    // Append the newsletter link after the table if it doesn't exist
    if (!newsletterLink) {
        const tableContainer = document.getElementById('result-table');
        newsletterLink = document.createElement('p');
        newsletterLink.innerHTML = '<a href="https://osintnewsletter.com" target="_blank">Subscribe to The OSINT Newsletter</a>';
        newsletterLink.id = 'newsletter-link';
        tableContainer.parentNode.insertBefore(newsletterLink, tableContainer.nextSibling);
    }
}
