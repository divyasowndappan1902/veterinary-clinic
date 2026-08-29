import re

html_file = "c:/Users/Admin/Desktop/veternery/index.html"
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# Add blobs to hero
if '<section class="hero"' in content and '<div class="blob blob-1"></div>' not in content:
    content = content.replace('<section class="hero"', '<section class="hero" style="position: relative; overflow: hidden;"')
    content = content.replace('<div class="container hero-container">', '<div class="blob blob-1"></div>\n        <div class="blob blob-2"></div>\n        <div class="container hero-container">')

# Hero animations
content = content.replace('<div class="hero-content">', '<div class="hero-content" data-aos="fade-right" data-aos-duration="1000">')
content = content.replace('<div class="hero-image-box">', '<div class="hero-image-box" data-aos="fade-left" data-aos-duration="1200">')
content = content.replace('<div class="hero-image">', '<div class="hero-image img-zoom-hover">')

# About section animations
content = content.replace('<section class="about-us"', '<section class="about-us" data-aos="fade-up"')
content = content.replace('<div class="about-image-box">', '<div class="about-image-box img-zoom-hover" data-aos="slide-right">')
content = content.replace('<div class="about-content">', '<div class="about-content" data-aos="slide-left">')
content = content.replace('<ul class="about-features">', '<ul class="about-features" data-aos="fade-up" data-aos-delay="200">')

# Services Animations (differentiate them)
if 'data-aos="fade-up"' not in content.split('<!-- Service 1 -->')[1][:100]:
    content = content.replace('<!-- Service 1 -->\n                <div class="service-card">', '<!-- Service 1 -->\n                <div class="service-card" data-aos="fade-up" data-aos-delay="100">')
    content = content.replace('<!-- Service 2 -->\n                <div class="service-card">', '<!-- Service 2 -->\n                <div class="service-card" data-aos="zoom-in" data-aos-delay="200">')
    content = content.replace('<!-- Service 3 -->\n                <div class="service-card">', '<!-- Service 3 -->\n                <div class="service-card" data-aos="fade-left" data-aos-delay="300">')
    content = content.replace('<!-- Service 4 -->\n                <div class="service-card">', '<!-- Service 4 -->\n                <div class="service-card" data-aos="fade-right" data-aos-delay="100">')
    content = content.replace('<!-- Service 5 -->\n                <div class="service-card">', '<!-- Service 5 -->\n                <div class="service-card" data-aos="flip-left" data-aos-delay="200">')
    content = content.replace('<!-- Service 6 -->\n                <div class="service-card">', '<!-- Service 6 -->\n                <div class="service-card" data-aos="fade-up" data-aos-delay="300">')

# Why Choose Us
content = content.replace('<section class="why-choose-us"', '<section class="why-choose-us" data-aos="fade-up"')
content = content.replace('<div class="choose-image">', '<div class="choose-image img-zoom-hover" data-aos="zoom-in">')
content = content.replace('<div class="choose-content">', '<div class="choose-content" data-aos="fade-left">')

# Core Features
content = content.replace('<section class="core-features"', '<section class="core-features" data-aos="fade-up"')
content = content.replace('<!-- Feature 1 -->\n                <div class="feature-card">', '<!-- Feature 1 -->\n                <div class="feature-card icon-bounce" data-aos="fade-up" data-aos-delay="100">')
content = content.replace('<!-- Feature 2 -->\n                <div class="feature-card">', '<!-- Feature 2 -->\n                <div class="feature-card icon-slide" data-aos="fade-up" data-aos-delay="200">')
content = content.replace('<!-- Feature 3 -->\n                <div class="feature-card">', '<!-- Feature 3 -->\n                <div class="feature-card icon-scale" data-aos="fade-up" data-aos-delay="300">')
content = content.replace('<!-- Feature 4 -->\n                <div class="feature-card">', '<!-- Feature 4 -->\n                <div class="feature-card icon-rotate" data-aos="fade-up" data-aos-delay="400">')

# Products
content = content.replace('<section class="popular-products"', '<section class="popular-products" data-aos="fade-up"')

# Pricing - Add premium class to Standard
content = content.replace('<!-- Standard Plan -->\n                <div class="pricing-card">', '<!-- Standard Plan -->\n                <div class="pricing-card premium">')
content = content.replace('<!-- Basic Plan -->\n                <div class="pricing-card">', '<!-- Basic Plan -->\n                <div class="pricing-card" data-aos="fade-right">')
content = content.replace('<!-- Premium Plan -->\n                <div class="pricing-card">', '<!-- Premium Plan -->\n                <div class="pricing-card" data-aos="fade-left">')

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("index.html updated successfully with premium animations.")
