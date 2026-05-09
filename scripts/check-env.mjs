const env = process.env;

const REQUIRED_URLS = ["JUDGE_URL", "JUDGE_RUN_URL"];
const OPTIONAL_POSITIVE_INTS = [
  "JUDGE_PORT",
  "JUDGE_MAX_CONCURRENT_JOBS",
  "JUDGE_MAX_CODE_BYTES",
  "JUDGE_MAX_STDIN_BYTES",
  "JUDGE_MAX_BODY_BYTES",
  "JUDGE_MAX_OUTPUT_BYTES",
  "JUDGE_RATE_LIMIT_WINDOW_MS",
  "JUDGE_RATE_LIMIT_MAX"
];
const OPTIONAL_POSITIVE_FLOATS = ["JUDGE_JOB_ACQUIRE_TIMEOUT_S"];
const SOCIAL_PROVIDER_GROUPS = [
  {
    label: "Kakao",
    names: ["KAKAO_REST_API_KEY", "KAKAO_REDIRECT_URI"],
    optional: ["KAKAO_CLIENT_SECRET"],
    trigger: ["KAKAO_REST_API_KEY", "KAKAO_CLIENT_SECRET"]
  },
  {
    label: "Naver",
    names: ["NAVER_CLIENT_ID", "NAVER_CLIENT_SECRET", "NAVER_REDIRECT_URI"],
    optional: [],
    trigger: ["NAVER_CLIENT_ID", "NAVER_CLIENT_SECRET"]
  }
];

const errors = [];
const warnings = [];

for (const name of REQUIRED_URLS) {
  if (!env[name]) {
    errors.push(`${name} is required`);
    continue;
  }
  try {
    const url = new URL(env[name]);
    if (!["http:", "https:"].includes(url.protocol)) {
      errors.push(`${name} must use http or https`);
    }
  } catch {
    errors.push(`${name} must be a valid URL`);
  }
}

for (const name of OPTIONAL_POSITIVE_INTS) {
  if (!env[name]) continue;
  const value = Number(env[name]);
  if (!Number.isInteger(value) || value <= 0) {
    errors.push(`${name} must be a positive integer`);
  }
}

for (const name of OPTIONAL_POSITIVE_FLOATS) {
  if (!env[name]) continue;
  const value = Number(env[name]);
  if (!Number.isFinite(value) || value <= 0) {
    errors.push(`${name} must be a positive number`);
  }
}

if (env.JUDGE_USE_DOCKER && !["0", "1"].includes(env.JUDGE_USE_DOCKER)) {
  errors.push("JUDGE_USE_DOCKER must be 0 or 1");
}

if (env.JUDGE_ENABLE_GENERIC_FUZZ && !["0", "1"].includes(env.JUDGE_ENABLE_GENERIC_FUZZ)) {
  errors.push("JUDGE_ENABLE_GENERIC_FUZZ must be 0 or 1");
}

if (env.JUDGE_USE_DOCKER === "1" && !env.CODERUNNER_IMAGE) {
  warnings.push("CODERUNNER_IMAGE is not set; judge will use its built-in default image name");
}

if (env.NODE_ENV === "production" && env.JUDGE_USE_DOCKER === "0") {
  errors.push("JUDGE_USE_DOCKER=0 is not allowed for production");
}

for (const group of SOCIAL_PROVIDER_GROUPS) {
  const touched = group.trigger.some((name) => !!env[name]);
  if (!touched) continue;
  for (const name of group.names) {
    if (!env[name]) errors.push(`${name} is required when ${group.label} login is configured`);
  }
  for (const name of group.names.filter((name) => name.endsWith("_REDIRECT_URI"))) {
    if (!env[name]) continue;
    try {
      const url = new URL(env[name]);
      if (!["http:", "https:"].includes(url.protocol)) {
        errors.push(`${name} must use http or https`);
      }
    } catch {
      errors.push(`${name} must be a valid URL`);
    }
  }
}

for (const warning of warnings) {
  console.warn(`[warn] ${warning}`);
}

if (errors.length > 0) {
  console.error("Environment check failed:");
  for (const error of errors) {
    console.error(`- ${error}`);
  }
  process.exit(1);
}

console.log("Environment check passed.");
