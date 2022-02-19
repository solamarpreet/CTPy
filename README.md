<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GPLv3 License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/solamarpreet/CTPy">
    <img src="images/logo.png" alt="Logo" width="100" height="60">
  </a>

<h3 align="center">Capture The Python</h3>

  <p align="center">
    CTPy is a series of Capture the Flag styled challenges for Python learners
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>




<!-- GETTING STARTED -->
## Getting Started

For absolute beginners or those who don't wish to install the game server locally, I have hosted the game server on my own vps. To get started simply

1. Clone the repo and cd into the folder
   ```sh
   git clone https://github.com/solamarpreet/CTPy.git && cd CTPy
   ```
2. Start the Python shell
   ```sh
   python3
   ```
3. Import the ctpy.py file into the Python shell
   ```py
   from ctpy import *
   ```
4. Fetch Question 1 and start playing :)
   ```py
   game.question(1)
   ```

### Usage

In order to play you need to make use of the **game** object that has already been initialized for you. This **game** object has 3 methods available which you need to use.

1. **game.question()** : This method pulls the question text from the server and displays it on the console. It accepts one parameter i.e Question Number
   ```py
   game.question(1)
   ```
2. **game.data()** : This method fetches the data associated with the Question. It accepts one parameter i.e Question Number
   ```py
   game.data(1)
   ```
3. **game.answer()** : This method submits your answer to the server and returns a string telling you if your answer was correct or incorrect. It accepts 2 parameters i.e The Question Number you are submitting the answer for and the answer itself.
   ```py
   game.answer(1, 'This is the answer')
   ```
   or
   ```py
   game.answer(1, x)
   ```
   where x is a variable containing the answer.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- HOSTING YOUR OWN SERVER -->
## Hosting your own server

### Prerequisites

The following external dependancies need to be pre-installed in order to host your own server.
* flask
  ```sh
  pip install flask
  ```

### Installation

1. Clone the repo and cd into the folder
   ```sh
   git clone https://github.com/solamarpreet/CTPy.git && cd CTPy
   ```
2. Start the game server
   ```sh
   python3 server/ctpy-server.py
   ```
3. Open a new terminal and edit the ctpy.py file in the text editor of your choice
   ```sh
   nano ctpy.py
   ```
4. Comment the last line as follows and create a new line with the url of your own server that flask provides you in Step 2
   ```nano
   # game = Game('http://ctpy.exoton.org')
   game = Game('http://127.0.0.1')
   ```
5. Save the ctpy file, start the Python shell and import the ctpy.py file as a module and start playing
   ```py
   from ctpy import *
   game.question(1)
   ```

<p align="right">(<a href="#top">back to top</a>)</p>




<!-- ROADMAP -->
## Roadmap

- [ ] Dynamic question data to ensure solutions are obtained in a programatic fashion
- [ ] Segregated beginner, intermediate and advanced challenge paths

See the [open issues](https://github.com/solamarpreet/CTPy/issues) for a full list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Please contribute additional quality questions/challenges so that Python beginners can continue to benefit from this project. If you have a question that you wish to add, please fork the repo, add your code and create a pull request. You can also simply open an issue with the tag "question".




<!-- LICENSE -->
## License

Distributed under the GPLv3 License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Amarpreet Singh - solamarpreet@protonmail.com

Portfolio & Blog: [https://solamarpreet.github.io](https://solamarpreet.github.io)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Python Discord](https://www.pythondiscord.com)
* [Flaticon](https://www.flaticon.com)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/solamarpreet/CTPy.svg?style=for-the-badge
[contributors-url]: https://github.com/solamarpreet/CTPy/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/solamarpreet/CTPy.svg?style=for-the-badge
[forks-url]: https://github.com/solamarpreet/CTPy/network/members
[stars-shield]: https://img.shields.io/github/stars/solamarpreet/CTPy.svg?style=for-the-badge
[stars-url]: https://github.com/solamarpreet/CTPy/stargazers
[issues-shield]: https://img.shields.io/github/issues/solamarpreet/CTPy.svg?style=for-the-badge
[issues-url]: https://github.com/solamarpreet/CTPy/issues
[license-shield]: https://img.shields.io/github/license/solamarpreet/CTPy.svg?style=for-the-badge
[license-url]: https://github.com/solamarpreet/CTPy/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
