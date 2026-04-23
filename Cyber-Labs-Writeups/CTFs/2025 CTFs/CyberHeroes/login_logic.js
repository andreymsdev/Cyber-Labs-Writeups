/**
 * Vulnerable login logic found in login.html
 * Challenge: TryHackMe - CyberHeros
 * * Vulnerability: Hardcoded credentials and client-side authentication.
 */

// Original obfuscated check:
// if (a.value=="h3ck3rBoi" & b.value==RevereString("54321@terceSrepuS"))

const credentials = {
    username: "h3ck3rBoi",
    password: "SuperSecret@12345" // Result of RevereString("54321@terceSrepuS")
};

console.log(`Discovered Credentials -> User: ${credentials.username} | Pass: ${credentials.password}`);