# Web Scraper

## Author: Brandon Mizutani

Version: 1.0.0 (PR URL: [PR URL](https://github.com/bran2miz/web-scraper/pull/3))

## Overview

This lab assignment required us to create a web scraper that can automate the process of manually using the site.

## Getting Started

### Lab 17

This web scraper is able to:

1.Scrape a Wikipedia page (Cnut the Great) and record which passages need citations.

2.Report the number of citations needed

3.Identify these cases of citations needed and include the relevant passages.

The web scraper also includes:

- A function named
get_citations_needed_count, which takes a url and returns an integer

- A functions named get_citations_needed_report, which takes a url and returns a string. The string is formatted with each citations need on its own line.

## Architecture

Python, Poetry, Requests

## Change Log

01-22-22: All three tests are passing, and the citation count and report functions are working.

## Credit and Collaborations

Eddie Ponce

Alex Payne

Connor Boyce

Roger Huba
