# Project: Password Checker
# Check to see if your passwords have been exposed in a data breach
# Terminal Input: python3 passwordchecker.py password1 password2 ...

import hashlib
import sys

import requests


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    api_response = requests.get(url)

    if api_response.status_code != 200:
        raise RuntimeError(
            f'Error Fetching: {api_response.status_code}, '
            'check the api and try again.')
    return api_response


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())

    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1_password[:5], sha1_password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)

        if count:
            print(
                f'MATCH FOUND! The password \"{password}\" has been leaked '
                f'{count} times.')
        else:
            print(f'NO MATCH FOUND! The password \"{password}\" is safe.')
    return 'Done!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
