import { defineCollection, z } from "astro:content";

const dataset = defineCollection({
  schema: z.object({
    title: z.string(),
    description: z.string(),
    source: z.string(),
    endpoint: z.string(),
    rows: z.number(),
    category: z.string(),
    sourceUrl: z.string().url().optional(),
  }),
});

export const collections = { dataset };
