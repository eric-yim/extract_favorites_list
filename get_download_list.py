from bs4 import BeautifulSoup
import argparse

COMMENT_CONTAINER = ['div',{'data-e2e':'favorites-item'}]
def ap():
    parser = argparse.ArgumentParser(description='A simple CLI tool.')

    # Add an argument
    parser.add_argument('--html_txt', type=str, help='local path to downloaded html code' ,required=True)
    parser.add_argument('--output_txt', type=str, help='save list to txt' ,default='download_list.txt')

    # Parse the command-line arguments
    return parser.parse_args()

def main(args):
    print(f"Parsing html {args.html_txt}")
    soup = BeautifulSoup(open(args.html_txt,'r'),'html.parser')
    containers = soup.find_all(*COMMENT_CONTAINER)
    print(f"Found videos: {len(containers)}")
    all_links = []
    for container in containers:
        links = container.find_all('a')
        assert len(links)==1
        all_links.append(links[0]['href'])

    with open(args.output_txt,'w') as f:
        for link in all_links:
            f.write(link)
            f.write('\n')
    print(f"Wrote to {args.output_txt}")
if __name__=='__main__':
    args = ap()
    main(args)