FROM node:18-alpine AS base

WORKDIR /app

COPY package.json yarn.lock* package-lock.json* pnpm-lock.yaml* ./
RUN \
  if [ -f yarn.lock ]; then \
    yarn install --frozen-lockfile; \
  elif [ -f package-lock.json ]; then \
    npm install; \
  elif [ -f pnpm-lock.yaml ]; then \
    npm install -g pnpm && pnpm install; \
  else \
    echo "No lock file found. Please provide yarn.lock, package-lock.json, or pnpm-lock.yaml." && exit 1; \
  fi

COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm","start"]