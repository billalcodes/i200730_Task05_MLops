# Use the official Node.js image as the base image
FROM node:latest

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the frontend files to the working directory
COPY . .

# Build the frontend application
RUN npm run build

# Expose port 3000 (assuming your frontend app runs on port 3000)
EXPOSE 3000

# Command to start the frontend server
CMD ["npm", "start"]
