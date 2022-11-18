<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



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
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/TuWeile/SSB-Determinator">
    <img src="resources/bond.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Singapore Savings Bonds (SSB) Calculator</h3>

  <p align="center">
    SSB calculation and determination of next month's SSB through SGS bond references, spline interpolation, and step-up adjustments
    <br />
    <a href="https://github.com/TuWeile/SSB-Determinator"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/TuWeile/SSB-Determinator">Documentation</a>
    ·
    <a href="https://github.com/TuWeile/SSB-Determinator/issues">Report Bug</a>
    ·
    <a href="https://github.com/TuWeile/SSB-Determinator/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
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



<!-- ABOUT THE PROJECT -->
## About The Project

[![Illustration of SSB Bond Yield Website][product-screenshot]](https://github.com/TuWeile/SSB-Determinator)

This repository serves to provide an estimation to determine for the next month's average return per year (%) through
obtaining the simple moving average of the daily SGS benchmark yields (1Y, 2Y, 5Y, 10Y) from the current month. Inspired
by the [MAS calculations and technical specifications][MAS-resources] and further independent research on 
[the determination of the valuation of Singapore Savings Bonds][SMU-resources] and 
[another similar report on the estimation of effective SSB rates from SGS benchmark yields][blog-resources],
it is hoped that the optimization of the step-up adjustments and the basis application into Python / C++ libraries will
be able to contribute further into developing future predictions and estimations into the upcoming SSB bond yield model.

Documentation and specific details can be found [here][medium] on Medium.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python.lg]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/TuWeile/SSB-Determinator.svg?style=for-the-badge
[contributors-url]: https://github.com/TuWeile/SSB-Determinator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/TuWeile/SSB-Determinator.svg?style=for-the-badge
[forks-url]: https://github.com/TuWeile/SSB-Determinator/network/members
[stars-shield]: https://img.shields.io/github/stars/TuWeile/SSB-Determinator.svg?style=for-the-badge
[stars-url]: https://github.com/TuWeile/SSB-Determinator/stargazers
[issues-shield]: https://img.shields.io/github/issues/TuWeile/SSB-Determinator.svg?style=for-the-badge
[issues-url]: https://github.com/TuWeile/SSB-Determinator/issues
[license-shield]: https://img.shields.io/github/license/TuWeile/SSB-Determinator.svg?style=for-the-badge
[license-url]: https://github.com/TuWeile/SSB-Determinator/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/tuweile/
[product-screenshot]: resources/SSB-description.gif
[Python.lg]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[MAS-resources]: https://www.mas.gov.sg/-/media/MAS/SGS/SGS-Announcements-pdf/SSB-PDF/FAQ/20190201-SSB-Technical-specifications_SRS.pdf
[SMU-resources]: https://ink.library.smu.edu.sg/cgi/viewcontent.cgi?article=7615&context=lkcsb_research
[blog-resources]: https://meltec22.wixsite.com/finlitsg/post/estimating-effective-ssb-rates-from-sgs-benchmark-yields
[medium]: https://medium.com/@tuweile
