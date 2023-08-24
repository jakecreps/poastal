let newsletterLink = null;

document.getElementById('email').addEventListener('keypress', async function (event) {
    if (event.key === 'Enter') {
        const email = this.value;
        const url = `http://localhost:8080/?email=${encodeURIComponent(email)}`;

        // Clear table content
        document.getElementById('result').innerHTML = '';
        document.getElementById('image-container').innerHTML = '';

        // Show loading element
        document.getElementById('loading').classList.remove('hidden');
        // Hide table header
        document.getElementById('result-table').querySelector('thead').innerHTML = '';

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

    let nameRowCreated = false;

    // Create and insert the Name row at the top of the table
    const nameRow = document.createElement('tr');
    const namePlatformCell = document.createElement('td');
    namePlatformCell.textContent = 'Name';
    nameRow.appendChild(namePlatformCell);
    const nameResultCell = document.createElement('td');
    nameRow.appendChild(nameResultCell);
    resultTable.insertBefore(nameRow, resultTable.firstChild);

    for (const category in data) {
        if (category === 'profiles') {
            for (const platform in data[category]) {
                const row = document.createElement('tr');
                const platformCell = document.createElement('td');
                platformCell.textContent = platform;
                row.appendChild(platformCell);

                const resultCell = document.createElement('td');
                const iconWrapper = document.createElement('div');
                const icon = document.createElement('img');
                icon.width = 16;
                icon.height = 16;

                if (data[category][platform] === 'true') {
                    icon.src = './img/true.png';
                    iconWrapper.setAttribute('data-tooltip', 'Profile found');
                } else if (data[category][platform] === 'unknown') {
                    icon.src = './img/unknown.png';
                    iconWrapper.setAttribute('data-tooltip', 'Profile status unknown');
                } else {
                    icon.src = './img/false.png';
                    iconWrapper.setAttribute('data-tooltip', 'Profile not found');
                }

                iconWrapper.appendChild(icon);
                resultCell.appendChild(iconWrapper);
                row.appendChild(resultCell);

                resultTable.appendChild(row);
            }
        } else {
            if (category !== 'Image' && category !== 'Duolingo Name' && category !== 'GitHub Name') {
                const row = document.createElement('tr');
                const platformCell = document.createElement('td');
                platformCell.textContent = category;
                row.appendChild(platformCell);

                const resultCell = document.createElement('td');
                const iconWrapper = document.createElement('div');
                const icon = document.createElement('img');
                icon.width = 16;
                icon.height = 16;

                if (category === 'Location') {
                    if (data[category] === 'N/A') {
                        icon.src = './img/false.png';
                        iconWrapper.setAttribute('data-tooltip', 'No location found');
                        iconWrapper.appendChild(icon);
                        resultCell.appendChild(iconWrapper);
                    } else {
                        resultCell.textContent = data[category];
                    }
                } else {
                    if (data[category] === 'true') {
                        icon.src = './img/true.png';
                        if (category === 'Deliverable') {
                            iconWrapper.setAttribute('data-tooltip', 'Email is deliverable');
                        } else if (category === 'Disposable') {
                            iconWrapper.setAttribute('data-tooltip', 'Email is disposable');
                        } else if (category === 'Spam') {
                            iconWrapper.setAttribute('data-tooltip', 'Email is spam');
                        }
                    } else {
                        icon.src = './img/false.png';
                        if (category === 'Deliverable') {
                            iconWrapper.setAttribute('data-tooltip', 'Email is not deliverable');
                        } else if (category === 'Disposable') {
                            iconWrapper.setAttribute('data-tooltip', 'Email is not disposable');
                        } else if (category === 'Spam') {
                            iconWrapper.setAttribute('data-tooltip', 'Email is not spam');
                        }
                    }
                    iconWrapper.appendChild(icon);
                    resultCell.appendChild(iconWrapper);
                }
                row.appendChild(resultCell);
                resultTable.appendChild(row);
            }
        }
    }

    let names = [];

    if (data['Duolingo Name'] !== 'N/A') {
        names.push(data['Duolingo Name']);
    }
    if (data['GitHub Name'] !== 'N/A') {
        names.push(data['GitHub Name']);
    }

    if (names.length > 0) {
        nameResultCell.textContent = names.join(', ');
    } else {
        const iconWrapper = document.createElement('div');
        const icon = document.createElement('img');
        icon.width = 16;
        icon.height = 16;
        icon.src = './img/false.png';
        iconWrapper.setAttribute('data-tooltip', 'No information found');
        iconWrapper.appendChild(icon);
        nameResultCell.appendChild(iconWrapper);
    }

    document.getElementById('result-table').querySelector('thead').classList.remove('hidden');

    if (!newsletterLink) {
        const tableContainer = document.getElementById('result-table');
        newsletterLink = document.createElement('p');
        newsletterLink.innerHTML = '<a href="https://osintnewsletter.com" target="_blank">Subscribe to The OSINT Newsletter</a>';
        newsletterLink.id = 'newsletter-link';
        tableContainer.parentNode.insertBefore(newsletterLink, tableContainer.nextSibling);
    }

    if (data.Image && data.Image !== 'false') {
        const imageContainer = document.getElementById('image-container');
        imageContainer.innerHTML = '';

        if (data.Image) {
            for (const platform in data.Image) {
                // Add a check to ensure the image URL is not 'false' for Gravatar
                if (data.Image[platform] !== 'false' && data.Image[platform] !== null) {
                    let imageUrl = data.Image[platform];

                    if (platform === 'Duolingo') {
                        imageUrl = 'https:' + imageUrl + '/xlarge';
                    } else if (platform === 'Gravatar') {
                        imageUrl = imageUrl + '?s=400';
                    }

                    // Only display the image if the URL is not 'N/A'
                    if (imageUrl !== 'N/A') {
                        const img = document.createElement('img');
                        img.src = imageUrl;
                        img.alt = `${platform} profile image`;
                        img.width = 175;
                        img.height = 175;

                        imageContainer.appendChild(img);
                    }
                }
            }
        }
    } else {
        // Clear image container if no image is found
        document.getElementById('image-container').innerHTML = '';
    }
}
