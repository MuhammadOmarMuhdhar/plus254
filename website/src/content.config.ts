import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const dataset = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/dataset" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    source: z.string(),
    endpoint: z.string(),
    rows: z.number(),
    topic: z.string(),
    sourceUrl: z.string().url().optional(),
  }),
});

export const collections = { dataset };
