import requests
from bs4 import BeautifulSoup


def get_html_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")
    else:
        return response.text

if __name__ == '__main__':
    print("Enter leetcode profile login to get information.")

    login = input('Login: ')

    html_doc = get_html_page(f'https://leetcode.com/{login}/')

    soup = BeautifulSoup(html_doc, 'html.parser')

    rank = soup.find(string="Rank")
    rank_value = rank.next_element.next_element.string

    if rank_value:
        print(f"{login}'s rank: {rank_value}")

    problem_solved = soup.find(class_='text-[24px] font-medium text-label-1 dark:text-dark-label-1').string

    if problem_solved:
        print(f"Problems solved: {problem_solved}")
    else:
        print("Could not get number of solved problems")
    
    easy_problems = soup.find(string="Easy")
    easy_problems_count = easy_problems.next_element.next_element.string

    if easy_problems_count:
        print(f"Easy problems: {easy_problems_count}")
    
    medium_problems = soup.find(string="Medium")
    medium_problems_count = medium_problems.next_element.next_element.string

    if medium_problems_count:
        print(f"Medium problems: {medium_problems_count}")
    
    hard_problems = soup.find(string="Hard")
    hard_problems_count = hard_problems.next_element.next_element.string

    if hard_problems_count:
        print(f"Hard problems: {hard_problems_count}")
