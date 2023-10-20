t allowedDomains = ['example.com', 'subdomain.example.com'];

function isAllowedDomain() {
	    const referrer = document.referrer;
	    if (!referrer) return false;
	    const referrerURL = new URL(referrer);
	    return allowedDomains.includes(referrerURL.hostname);
}

if (!isAllowedDomain()) {
	    window.location.href = 'https://example.com/access-denied.html'; // Redirect to an access denied page
	//}
	//
