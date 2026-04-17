import { mkdir, readFile, writeFile } from "node:fs/promises";
import path from "node:path";

const rootDir = path.resolve(process.cwd(), "..", "database");

const storeFiles = {
  bookings: path.join(rootDir, "bookings.json"),
  contacts: path.join(rootDir, "contacts.json"),
  newsletter: path.join(rootDir, "newsletter.json"),
};

async function ensureStoreFile(storeName) {
  const filePath = storeFiles[storeName];

  if (!filePath) {
    throw new Error(`Unknown store: ${storeName}`);
  }

  await mkdir(rootDir, { recursive: true });

  try {
    await readFile(filePath, "utf8");
  } catch {
    await writeFile(filePath, "[]\n", "utf8");
  }

  return filePath;
}

export async function readStore(storeName) {
  const filePath = await ensureStoreFile(storeName);
  const raw = await readFile(filePath, "utf8");

  try {
    const parsed = JSON.parse(raw);
    return Array.isArray(parsed) ? parsed : [];
  } catch {
    return [];
  }
}

export async function appendStoreItem(storeName, item) {
  const filePath = await ensureStoreFile(storeName);
  const items = await readStore(storeName);

  items.unshift(item);

  await writeFile(filePath, `${JSON.stringify(items, null, 2)}\n`, "utf8");

  return item;
}
