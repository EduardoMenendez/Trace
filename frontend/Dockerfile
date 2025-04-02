# frontend/Dockerfile
FROM node:20

WORKDIR /app

# Copy package.json and lock file first (for layer caching)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the frontend source code
COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]
