#!/bin/bash
curl -sG "https://api.mapbox.com/matching/v5/mapbox/driving/""$1"";""$2""?steps=true&access_token=pk.eyJ1IjoibWF0aWFzaXJhbGEyMDEyIiwiYSI6ImNrMnA4bjVuczAxb3ozZW13cXd1anRibjQifQ.0qbvkY9jEu9bOt54qylpmw" 
