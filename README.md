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

Once I have taken the time to complete up the writings, documentation and its specific details can be found [here][medium] on Medium.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python.lg]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

In order to get the project running locally within your computer, follow these prerequisites below:

### Prerequisites

* List of Python packages to install
  ```sh
  numpy
  pandas
  configparser
  ```

### Installation

1. Determine the <strong>month</strong> of the SSB bond you want to estimate. If you want to estimate for the December 
SSB bond, you will need to obtain the data for the month of <strong>October</strong> SGS reference yields. This is because
it takes a month to bid for the SSB (Nov 1 to Nov 25) after collecting the data from October, and it is only issued on the
first day of the next month after the bidding period is over (Dec 1, hence the term "December SSB bond").

2. Download the data from the [SGS Prices and Yields - Benchmark Issues][MAS-website] here, with the specifications that:
   ```shell
   Frequency: Daily
   
   Average Buying Rates of Govt Securities Dealers: [1-Year T-Bill Yield, 2-Year Bond Yield, 5-Year Bond Yield, 10-Year Bond Yield]
   ```
   You may refer to the above gif illustration to download the data as shown above.

3. Clone the repo and place the data you have downloaded in the /data directory. You may find sample data as shown within the
directory specified. Once completed, configure the `config.ini` file such that the data variable is pointing to the file added.

4. Start up your IDE (PyCharm), and configure the working directory within the configuration to point towards the `/path/to/SSB-Determiantor`
directory. Once completed, you can run `main.py` to execute the script.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

When using this repository, it is generally advisable to execute the repository on the last working day of the calendar month
for the best results as the [SGS Prices and Yields - Benchmark Issues][MAS-website] is updated daily. I will eventually consider
adding in new features to predict and forecast acceptable daily bond yields ahead of time, but at the moment this would require
research as multiple parameters will need to be considered for such an evaluation.

Furthermore, when running this repository, please keep into consideration of the [CME FedWatch Tool][CME-Tool] as the SGS Bond
Yields closely follows the U.S. Fed interest rates and can serve as an important guidance in forecasting future bond yields.

As for the adjustments within the technical specifications, please do allow for the adjustments of the coupons to differ by
up to ±0.06%. While this is not within the acceptable range of ±0.03% from the technical specifications, nevertheless I do
intend to optimize the calculations further to meet with the rounding of the computation of the step-up coupons.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are <strong>greatly appreciated</strong>.

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

Distributed under the BSD 3-Clause "New" License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Tu Weile - [LinkedIn][linkedin-url] - tuweile.sg@gmail.com

Project Link: [https://github.com/TuWeile/SSB-Determinator](https://github.com/TuWeile/SSB-Determinator)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Monetary Authority of Singapore. (2019). Singapore Savings Bonds: Technical Specifications.][MAS-resources]
* [Lim, K. G. (2021). Bermudan option in Singapore Savings Bonds. Review of Derivatives Research, 24(1), 31-54.][SMU-resources]
* [Melvin. (2022). Estimating effective SSB rates from SGS Benchmark Yields. Financial Literacy Singapore.][blog-resources]

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
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/tuweile/
[product-screenshot]: resources/SSB-description.gif
[Python.lg]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[MAS-resources]: https://www.mas.gov.sg/-/media/MAS/SGS/SGS-Announcements-pdf/SSB-PDF/FAQ/20190201-SSB-Technical-specifications_SRS.pdf
[SMU-resources]: https://ink.library.smu.edu.sg/cgi/viewcontent.cgi?article=7615&context=lkcsb_research
[blog-resources]: https://meltec22.wixsite.com/finlitsg/post/estimating-effective-ssb-rates-from-sgs-benchmark-yields
[medium]: https://medium.com/@tuweile
[MAS-website]: https://eservices.mas.gov.sg/statistics/fdanet/BenchmarkPricesAndYields.asp
[CME-Tool]: https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html