# Use the official Nginx image from the Docker Hub
FROM nginx:latest

# Copy your HTML file into the default Nginx directory
COPY index.html /usr/share/nginx/html/index.html

# Expose port 1111 to the host
EXPOSE 1111

# Run Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
