import re
import json
import aiohttp
import asyncio
from unidecode import unidecode  # Import the unidecode library

# Define a regular expression pattern to match the URLs
pattern = r'https://(\w+)\.inhire\.app'

# Read the input text from a file
with open('input.txt', 'r') as file:
    text = file.read()

# Find all matches in the text
matches = re.findall(pattern, text)

# Initialize a dictionary to store the job links and sum of jobs found
job_links = {}
job_sum = {}

async def fetch_data(subdomain):
    url = f'https://api.inhire.app/job-posts/public/pages/'
    headers = {"X-Tenant": subdomain}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                jobs = data.get('jobsPage', [])
                job_sum[subdomain] = len(jobs)

                for job in jobs:
                    job_id = job.get('jobId')
                    job_name = job.get('displayName')
                    
                    # Use unidecode to transliterate special characters
                    job_name = unidecode(job_name)
                    
                    # Remove any remaining special characters
                    job_name = re.sub(r'[^\w\s-]', '', job_name)
                    
                    # Replace spaces with hyphens and make lowercase
                    job_name = job_name.replace(" ", "-").lower()
                    
                    job_link = f'https://{subdomain}.inhire.app/vagas/{job_id}/{job_name}'
                    job_links[job_id] = job_link

async def main():
    tasks = [fetch_data(subdomain) for subdomain in matches]
    await asyncio.gather(*tasks)

    # Save the updated data to a JSON file
    with open('inhire_jobs.json', 'w') as json_file:
        json.dump(job_links, json_file, indent=4)

# Run the asynchronous code
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

# Print the sum of jobs found for each domain
for subdomain, count in job_sum.items():
    print(f'Domain: {subdomain}, Jobs Found: {count}')

print("Job links saved to 'inhire_jobs.json'")
