#!/usr/env/python 3
import os
import json
import hashlib
import datetime


def handler(event, context):

    try:

        # Console.WriteLine("Well Hello There!");
        print("Well Hello There!")
        # Console.WriteLine("The current time is " + DateTime.Now);
        print("The current time is " + datetime.datetime.now)

        print(event)
        body = json.loads(event.get('body', {}))

        pass_str = body.get('password', '')
        username = body.get('username', '')
        age_str = body.get('age', '0')

        # // Type your username and press enter
        # Console.WriteLine("Enter your name:");
        print("Username is:  " + str(username))

        # // Create a string variable and get user input from the keyboard and store it in the variable
        # string userName = Console.ReadLine();
       

        # Console.WriteLine("Enter your age:");
        # int age = Convert.ToInt32(Console.ReadLine());
        # Console.WriteLine("Your age is: " + age);
        age = int(age_str)
        print("Your age is: " + age)

        print('event   ', event)
        print('pass_str   ', pass_str)

        result = hashlib.md5(pass_str.encode())  # nosec CWE-327
        print('hash ', result.hexdigest())

        return {
            'statusCode': 200,
            'body': result.hexdigest()
        }

    except Exception as ex:

        return {
            'statusCode': 200,
            'body': 'Error: ' + ex.message
        }
