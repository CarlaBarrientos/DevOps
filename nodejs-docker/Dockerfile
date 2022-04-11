# Pulls the image from Dockerhub
FROM node:16
# Define env variables
ENV NODE_VERSION 16.14.2
# Create app directory
WORKDIR /app
# Copy package and package-lock to install app dependencies
COPY package*.json ./
# Install dependencies
RUN npm install
# Copy all the src folder to /app
COPY . .
# Expose the specified port
EXPOSE 3000
# Start the program when the container is ex
CMD [ "npm", "start" ]