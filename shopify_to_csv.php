<?php
define('CHARSET', 'UTF-8');
// ============================================================================
// CREATED BY  : JEROMIE KIRCHOFF
// DESCRPITION : PULL PRODUCTS FROM SHOPIFY ON BEHALF OF A CUSTOMER INTO CSV
// ============================================================================
// MODIFICATIONS: ADDED EXIT STATEMENT TO HELP WITH MISSING/ EXTRA PARAMETERS
//                ADDED COMMENTS TO BETTER DESCRIBE FUNCTIONS / BEHAVIOR
//                ADDED PRINT STATEMENTS TO SHOWCASE THE NUMBER OF RECORDS
//                AND TIME TAKING TO PULL.
//                CHANGED EVERYTHING TO CONVERT SYMBOLS TO HTMLSPECIALCHARS
//                THIS FIX ENCODING & ENCAPSULATING ISSUES.
// ============================================================================
// TODO: CUSTOMIZE FOR EACH NEED.
// ============================================================================

// ============================================================================
// STEP 1: ERROR HANDLING
// CHECK PARAMETERS - IF IT DOESN'T GET 3 OR 4 IT WILL BAIL OUT & SEND AN EMAIL
// PLEASE CHANGE Superman@Krypton.Universe TO YOUR EMAIL - ADDED THIS FOR SERVER SUPPORT MONITORING
// INCASE YOU CONFIGURED IT TO RUN FROM THE CRONTAB AND FUDGED IT.
// ============================================================================
switch (TRUE) {
case $_SERVER['argc'] == 0:
    // THIS SHOULD NEVER HAPPEN!  THIS SHOULD ALWAYS BE DEFINED AS THE FILENAME.
    error_log("Shopify: WARNING: THE IMPOSSIBLE HAPPEND. THIS HAS NO FILE NAME!",1,"Superman@Krypton.Universe","From: Superman@Krypton.Universe\r\nSubject: Shopify Error: " . $dateTime );
    exit("WARNING: THE IMPOSSIBLE HAPPEND. THIS HAS NO FILE NAME...\nSincerely,\nDisrupto Bot\n EXITING!\n");
    break;
case $_SERVER['argc'] == 1:
    error_log("Usage: Requires Shopify Key, Shopify Password, & Shopify Store Parameters. EXITING!",1,"Superman@Krypton.Universe","From: Superman@Krypton.Universe\r\nSubject: Shopify Error: " . $dateTime );
    exit("Usage: Requires Shopify Key, Shopify Password, & Shopify Store Parameters. EXITING!\n\n");
    break;
case $_SERVER['argc'] == 2:
    error_log("Usage: Requires Shopify Password, & Shopify Store Parameters. EXITING!",1,"Superman@Krypton.Universe","From: Superman@Krypton.Universe\r\nSubject: Shopify Error: " . $dateTime );
    exit("Usage: Requires Shopify Password, & Shopify Store Parameters. EXITING!\n\n");
    break;
case $_SERVER['argc'] == 3:
    error_log("Usage: Requires Shopify Store Parameter. EXITING!",1,"Superman@Krypton.Universe","From: Superman@Krypton.Universe\r\nSubject: Shopify Error: " . $dateTime );
    exit("Usage: Requires Shopify Store Parameter. EXITING!\n\n");
    break;
case $_SERVER['argc'] == 4:
    // ============================================================================
    // THIS IS THE APPROPRIATE AMOUNT OF PARAMS
    // ============================================================================
    // print($argv[3] . ' ' .date("Ymd_H_i_s") . ": Usage: Optional Parameter shopify_collection_id, Not Used.\n Continuing on...");
    break;
case $_SERVER['argc'] > 5:
    error_log("Usage: Received Too Many Parameters. EXITING!",1,"Superman@Krypton.Universe","From: Superman@Krypton.Universe\r\nSubject: Shopify Error: " . $dateTime );
    exit("Usage: Received Too Many Parameters. EXITING!\n\n");
    break;
};

// ============================================================================
// STEP 2: CREATE SHOPIFY CLASS
// ============================================================================
class Shopify {
    private $shopify_key;
    private $shopify_password;
    private $shopify_store;
    private $shopify_collection;
    public function __construct($key, $password, $store) {
        $this->shopify_key = $key;
        $this->shopify_password = $password;
        $this->shopify_store = $store;
        $this->shopify_url = 'https://' . $this->shopify_key . ':' . $this->shopify_password . '@' . $this->shopify_store . '.myshopify.com/admin/';
    }

    // ========================================================================
    // STEP 3: FUNCTION: MAKE REQUEST
    // ========================================================================
    public function makeRequest($url_slug, $method, $query) {

        $url = $this->shopify_url . $url_slug;
        $url = $this->curlAppendQuery($url, $query);
        $handle = curl_init($url);
        curl_setopt($handle, CURLOPT_RETURNTRANSFER, TRUE);
        $this->curlSetopts($handle, $method);
        // Get the HTML or whatever is linked in $URL.
        $response = curl_exec($handle);
        // Check for 404 (file not found).
        $httpCode = curl_getinfo($handle, CURLINFO_HTTP_CODE);

        // ====================================================================
        // PRINT ACTUAL ERROR CODES TO SCREEN.
        // Info: https://help.shopify.com/api/getting-started/response-status-codes
        // IGNORING ALL SUCCESSFUL LOOPED CONNECTIONS
        // ALL ERRORS WILL REPLY TO SCREEN WITH
        // ====================================================================
        switch (TRUE) {

        case $httpCode == 200:
            // print($argv[3] . ' ' .date("Ymd_H_i_s")
            // . ": Shopify API Responded With: "
            // . $httpCode
            // . ' '
            // . "OK - The request was successfully processed by Shopify.\n");
            break;
        case $httpCode == 201:
            // print($argv[3] . ' ' .date("Ymd_H_i_s")
            // . ": Shopify API Responded With: "
            // . $httpCode
            // . ' '
            // . "Created - The request has been fulfilled "
            // . " and a new resource has been created.\n");
            break;
        case $httpCode == 202:
            // print($argv[3] . ' ' .date("Ymd_H_i_s")
            // . ": Shopify API Responded With: "
            // . $httpCode
            // . ' '
            // . "Accepted - The request has been accepted, "
            // . "but not yet processed.\n");
            break;
        case $httpCode == 303:
            print($argv[3] . ' ' .date("Ymd_H_i_s")
                  . ": Shopify API Responded With: "
                  . $httpCode
                  . ' '
                  . "See Other - The response to the request can be found under a different URI in the Location header and can be retrieved using a GET method on that resource.\n\n EXITING\n\n");
            curl_close($handle);
            exit();
            break;
        case $httpCode == 400:
            print($argv[3] . ' ' .date("Ymd_H_i_s")
                  . ": Shopify API Responded With: "
                  . $httpCode
                  . ' '
                  . "Bad Request - The request was not understood by the server, generally due to bad syntax or because the Content-Type header was not correctly set to application/json.\nThis status is also returned when the request provides an invalid code parameter during the OAuth token exchange process.\n\n EXITING\n\n");
            curl_close($handle);
            exit();
            break;
        case $httpCode == 401:
            print($argv[3] . ' ' .date("Ymd_H_i_s")
                  . ": Shopify API Responded With: "
                  . $httpCode
                  . ' '
                  . "Unauthorized - The necessary authentication credentials are not present in the request or are incorrect.\n\n EXITING\n\n");
            curl_close($handle);
            exit();
            break;
        case $httpCode == 402:
            print($argv[3] . ' ' .date("Ymd_H_i_s")
                  . ": Shopify API Responded With: "
                  . $httpCode
                  . ' '
                  . "Payment Required - The requested shop is currently frozen.\n\n EXITING\n\n");
            curl_close($handle);
            exit();
            break;
        case $httpCode == 403:
            print($argv[3] . ' ' .date("Ymd_H_i_s")
                  . ": Shopify API Responded With: "
                  . $httpCode
                  . ' '
                  . "Forbidden - The server is refusing to respond to the request. This is generally because you have not requested the appropriate scope for this action.\n\n EXITING\n\n");
            curl_close($handle);
            exit();
            break;
        case $httpCode == 404:
            print($argv[3] . ' ' .date("Ymd_H_i_s")
                  . ": Shopify API Responded With: "
                  . $httpCode
                  . ' '
                  . "Not Found - The requested resource was not found but could be available again in the future.\n\n EXITING\n\n");
            curl_close($handle);
            exit();
            break;
        case $httpCode == 406:
            print($argv[3] . ' ' .date("Ymd_H_i_s")
                  . ": Shopify API Responded With: "
                  . $httpCode
                  . ' '
                  . "Not Acceptable - The requested resource is only capable of generating content not acceptable according to the Accept headers sent in the request.\n\n EXITING\n\n");
            curl_close($handle);
            exit();
            break;
        case $httpCode == 422:
            print($argv[3] . ' ' .date("Ymd_H_i_s")
                  . ": Shopify API Responded With: "
                  . $httpCode
                  . ' '
                  . "Un-processable Entity - The request body was well-formed but contains semantical errors. The response body will provide more details in the errors parameter.\n\n EXITING\n\n");
            curl_close($handle);
            exit();
            break;
        case $httpCode == 429:
            print($argv[3] . ' ' .date("Ymd_H_i_s")
                  . ": Shopify API Responded With: "
                  . $httpCode
                  . ' '
                  . "Too Many Requests - The request was not accepted because the application has exceeded the rate limit. See the API Call Limit documentation for a breakdown of Shopifys rate-limiting mechanism.\n\n EXITING\n\n");
            curl_close($handle);
            exit();
            break;
        case $httpCode == 500:
            print($argv[3] . ' ' .date("Ymd_H_i_s")
                  . ": Shopify API Responded With: "
                  . $httpCode
                  . ' '
                  . "Internal Server Error - An internal error occurred in Shopify. Please post to the API & Technology forum so that Shopify staff can investigate.\n\n EXITING\n\n");
            curl_close($handle);
            exit();
            break;
        case $httpCode == 501:
            print($argv[3] . ' ' .date("Ymd_H_i_s")
                  . ": Shopify API Responded With: "
                  . $httpCode
                  . ' '
                  . "501 Not Implemented - The requested endpoint is not available on that particular shop, e.g. requesting access to a Plus-specific API on a non-Plus shop. This response may also indicate that this endpoint is reserved for future use.\n\n EXITING\n\n");
            curl_close($handle);
            exit();
            break;
        case $httpCode == 503:
            print($argv[3] . ' ' .date("Ymd_H_i_s")
                  . ": Shopify API Responded With: "
                  . $httpCode
                  . ' '
                  . "Service Unavailable - The server is currently unavailable. Check the status page for reported service outages.\n\n EXITING\n\n");
            curl_close($handle);
            exit();
            break;
        case $httpCode == 504:
            print($argv[3] . ' ' .date("Ymd_H_i_s")
                  . ": Shopify API Responded With: "
                  . $httpCode
                  . ' '
                  . "Gateway Timeout - The request could not complete in time. Try breaking it down in multiple smaller requests.\n\n EXITING\n\n");
            curl_close($handle);
            exit();
            break;

        // ====================================================================
        // MY RULE: IT'S GOOD PRACTICE TO HAVE DEFAULTS TO CATCH THE UNEXPECTED
        // ====================================================================
        default:
            print('No Case found httpCode:'
                  . ' '
                  . $httpCode
                  . " EXITING."
                  .PHP_EOL);
            curl_close($handle);
            exit();
            break;
        }

        // ====================================================================
        // END OF HTTPS LOGGING
        // IF EVERYTHING PASSED WITH A 2XX THEN CLOSE THE HANDLE.
        // ====================================================================
        curl_close($handle);

        // ====================================================================
        // HANDLE THE RESPONSE HERE.
        // ====================================================================
        return $response;

        print($argv[3] . ' ' .date("Ymd_H_i_s") . ": Finished Make Request".PHP_EOL);

    }

    // ========================================================================
    // STEP 4: GET THE DATA FROM SHOPIFY (RUNS EACH CONNECTION THRU STEP 3)
    // ========================================================================
    public function getFeed($filename) {
        global $argc, $argv;

        // ====================================================================
        // expected format. ?collection_id=841564295
        if (!isset($argv[4]) || trim($argv[4]) === '') {
            $collection_id_for_array = '';
            print($argv[3] . ' ' .date("Ymd_H_i_s") . ": NO FILTER BY COLLECTION ID.PULLING ALL PRODUCTS for: " . $argv[3].PHP_EOL);
        } else {
            $collection_id_for_array = "?collection_id=" . $argv[4];
            print($argv[3] . ' ' .date("Ymd_H_i_s") . ": FILTERING RESULTS BASED ON COLLECTION: " . $argv[4].PHP_EOL);
            // print($argv[3] . ' ' .date("Ymd_H_i_s") . ": FILTERING RESULTS BASED ON COLLECTION String: " . $collection_id_for_array.PHP_EOL);
        };

            // ================================================================
            // Setting variables for looping.
            // Variables:
            // // products_count = to the max of the listed count for the client
            // // Shopify has a MAX limit of 250 per API Request
            // ================================================================

            $products_count = $this->makeRequest('products/count.json' . $collection_id_for_array, 'GET', array('published_status' => 'published'));
            $limit = 250;
            $products_count = json_decode($products_count, TRUE);
            $pages = ceil($products_count["count"] / $limit);
            $shop_get = $this->makeRequest('shop.json', 'GET', '');
            $shop_info = json_decode($shop_get, TRUE);
            $file = fopen($filename, "w");
            $headers = '"Product SKU Name","Product ID","Product Variant SKU","Product Variant Barcode","Product Variant ID","Product Variant Inventory Item ID","Product Title","Product Variant Title","Product Long Description","Product Short Description","Product brand","Product Category","Product Google Category","Product Keyword Tags","Product Variant Retail Price","Product Variant Sale Price","Product Variant Buy URL","Product Variant Image ID","Product Variant Image","Product Variant Large Image","Product Variant Medium Image","Product Variant Thumbnail Image","Product Variant Option 1","Product Variant Option 2","Product Variant Option 3","Product Variant Inventory Quantity","Product Variant Old Inventory Quantity","Product Variant Grams","Product Variant Weight","Product Variant Weight Unit","Product Variant Requires Shipping","Product Variant Fulfillment Service","Product Variant Inventory Management"'.PHP_EOL;
            fwrite($file, $headers);

        // ====================================================================
        // Logging for showing how many records are going to be pulled
        // ====================================================================
        print($argv[3] . ' ' .date("Ymd_H_i_s") . ": Total Unique Products Pull Count: " . $products_count['count'].PHP_EOL);
        print($argv[3] . ' ' .date("Ymd_H_i_s") . ": Start Looping thru Feed...".PHP_EOL);
        print($argv[3] . ' ' .date("Ymd_H_i_s") . ": Please be patient as this takes time"
              . "(This is estimated to take 1 min per 50K Product Variants)...".PHP_EOL);

        for ($i = 1; $i <= $pages; $i++) {

            if (($products_count['count'] - ($limit * $i)) > 0) {
                print($argv[3] . ' ' .date("Ymd_H_i_s") . ": Products Left To Pull : " . ($products_count['count'] - ($limit * ($i - 0))).PHP_EOL);
            } else {
                print($argv[3] . ' ' .date("Ymd_H_i_s") . ": Products Left To Pull : 0...Done!".PHP_EOL);
            };

            // ================================================================
            // MAKEREQUEST - PULL DATA AND BUILD ARRAY
            // ================================================================
            $products = $this->makeRequest('/products.json' . $collection_id_for_array, 'GET', array("limit" => $limit, "page" => $i, "published_status" => "published"));
            $products = json_decode($products, TRUE);

            // ================================================================
            // STRIP/CONVERT BAD BEHAVIOUR:
            // PLEASE REVIEW: AS THIS MAY NOT BEHAVE AS YOU INTEND, I MADE THIS TO HELP WITH EXCEL FILE OPENING (XLSX)
            // PLEASE REVIEW: SOME SYMBOLS THAT ARE NOT RENDERED TO THE NAKED EYE HAVE BEEN CONVERTED TO EMPTY STRINGS
            // PLEASE REVIEW: DESIGNED TO DIRECTLY FED TO A DATABASE FOR STORAGE AND RENDERING ON A WEB PAGE AS NEEDED.
            //     - CURLY APOSTROPHE
            //     - NEW LINES
            //     - COPYRIGHT
            //     - REGISTERED - TM - NBSP;
            //     - LEFT & RIGHT QUOTES.. ETC.
            // ================================================================
            $str_find_array    = array(       '?',   "\xc2\xbf", "\xc3\x80", "\xc3\x81", "\xc3\x82", "\xc3\x83", "\xc3\x84", "\xc3\x85", "\xc3\x86", "\xc3\x87", "\xc3\x88", "\xc3\x89", "\xc3\x8a", "\xc3\x8b", "\xc3\x8c", "\xc3\x8d", "\xc3\x8e", "\xc3\x8f", "\xc3\x90", "\xc3\x91", "\xc3\x92", "\xc3\x93", "\xc3\x94", "\xc3\x95", "\xc3\x96", "\xc3\x97", "\xc3\x98", "\xc3\x99", "\xc3\x9a", "\xc3\x9b", "\xc3\x9c", "\xc3\x9d", "\xc3\x9e", "\xc3\x9f", "\xc3\xa0", "\xc3\xa1", "\xc3\xa2", "\xc3\xa3", "\xc3\xa4", "\xc3\xa5", "\xc3\xa6", "\xc3\xa7", "\xc3\xa8", "\xc3\xa9", "\xc3\xaa", "\xc3\xab", "\xc3\xac", "\xc3\xad", "\xc3\xae", "\xc3\xaf", "\xc3\xb0", "\xc3\xb1", "\xc3\xb2", "\xc3\xb3", "\xc3\xb4", "\xc3\xb5", "\xc3\xb6", "\xc3\xb7", "\xc3\xb8", "\xc3\xb9", "\xc3\xba", "\xc3\xbb", "\xc3\xbc", "\xc3\xbd", "\xc3\xbe", "\xc3\xbf",  "\xc2\xad", "\xe2\x80\xa8",     "\xC2\x96",  "\xc2\x99",  "\xef\xa0\x80", "\xef\xa0\x81", "\xef\xa0\x82", "\xef\xa0\x83", "\xef\xa0\x84", "\xef\xa0\x85", "\xef\xa0\x86", "\xef\xa0\x87", "\xef\xa0\x88", "\xef\xa0\x89", "\xef\xa0\x8a", "\xef\xa0\x8b", "\xef\xa0\x8c", "\xef\xa0\x8d", "\xef\xa0\x8e", "\xef\xa0\x8f", "\xef\xa0\x90", "\xef\xa0\x91", "\xef\xa0\x92", "\xef\xa0\x93", "\xef\xa0\x94", "\xef\xa0\x95", "\xef\xa0\x96", "\xef\xa0\x97", "\xef\xa0\x98", "\xef\xa0\x99", "\xef\xa0\x9a", "\xef\xa0\x9b", "\xef\xa0\x9c", "\xef\xa0\x9d", "\xef\xa0\x9e", "\xef\xa0\x9f", "\xef\xa0\xa0", "\xef\xa0\xa1", "\xef\xa0\xa2", "\xef\xa0\xa3", "\xef\xa0\xa4", "\xef\xa0\xa5", "\xef\xa0\xa6", "\xef\xa0\xa7", "\xef\xa0\xa8", "\xef\xa0\xa9", "\xef\xa0\xaa", "\xef\xa0\xab", "\xef\xa0\xac", "\xef\xa0\xad", "\xef\xa0\xae", "\xef\xa0\xaf", "\xef\xa0\xb0", "\xef\xa0\xb1", "\xef\xa0\xb2", "\xef\xa0\xb3", "\xef\xa0\xb4", "\xef\xa0\xb5", "\xef\xa0\xb6", "\xef\xa0\xb7", "\xef\xa0\xb8", "\xef\xa0\xb9", "\xef\xa0\xba", "\xef\xa0\xbb", "\xef\xa0\xbc", "\xef\xa0\xbd", "\xef\xa0\xbe", "\xef\xa0\xbf", "\xef\xa1\x80", "\xef\xa1\x81", "\xef\xa1\x82", "\xef\xa1\x83", "\xef\xa1\x84", "\xef\xa1\x85", "\xef\xa1\x86", "\xef\xa1\x87", "\xef\xa1\x88", "\xef\xa1\x89", "\xef\xa1\x8a", "\xef\xa1\x8b", "\xef\xa1\x8c", "\xef\xa1\x8d", "\xef\xa1\x8e", "\xef\xa1\x8f", "\xef\xa1\x90", "\xef\xa1\x91", "\xef\xa1\x92", "\xef\xa1\x93", "\xef\xa1\x94", "\xef\xa1\x95", "\xef\xa1\x96", "\xef\xa1\x97", "\xef\xa1\x98", "\xef\xa1\x99", "\xef\xa1\x9a", "\xef\xa1\x9b", "\xef\xa1\x9c", "\xef\xa1\x9d", "\xef\xa1\x9e", "\xef\xa1\x9f", "\xef\xa1\xa0", "\xef\xa1\xa1", "\xef\xa1\xa2", "\xef\xa1\xa3", "\xef\xa1\xa4", "\xef\xa1\xa5", "\xef\xa1\xa6", "\xef\xa1\xa7", "\xef\xa1\xa8", "\xef\xa1\xa9", "\xef\xa1\xaa", "\xef\xa1\xab", "\xef\xa1\xac", "\xef\xa1\xad", "\xef\xa1\xae", "\xef\xa1\xaf", "\xef\xa1\xb0", "\xef\xa1\xb1", "\xef\xa1\xb2", "\xef\xa1\xb3", "\xef\xa1\xb4", "\xef\xa1\xb5", "\xef\xa1\xb6", "\xef\xa1\xb7", "\xef\xa1\xb8", "\xef\xa1\xb9", "\xef\xa1\xba", "\xef\xa1\xbb", "\xef\xa1\xbc", "\xef\xa1\xbd", "\xef\xa1\xbe", "\xef\xa1\xbf", "\xef\xa2\x80", "\xef\xa2\x81", "\xef\xa2\x82", "\xef\xa2\x83", "\xef\xa2\x84", "\xef\xa2\x85", "\xef\xa2\x86", "\xef\xa2\x87", "\xef\xa2\x88", "\xef\xa2\x89", "\xef\xa2\x8a", "\xef\xa2\x8b", "\xef\xa2\x8c", "\xef\xa2\x8d", "\xef\xa2\x8e", "\xef\xa2\x8f", "\xef\xa2\x90", "\xef\xa2\x91", "\xef\xa2\x92", "\xef\xa2\x93", "\xef\xa2\x94", "\xef\xa2\x95", "\xef\xa2\x96", "\xef\xa2\x97", "\xef\xa2\x98", "\xef\xa2\x99", "\xef\xa2\x9a", "\xef\xa2\x9b", "\xef\xa2\x9c", "\xef\xa2\x9d", "\xef\xa2\x9e", "\xef\xa2\x9f", "\xef\xa2\xa0", "\xef\xa2\xa1", "\xef\xa2\xa2", "\xef\xa2\xa3", "\xef\xa2\xa4", "\xef\xa2\xa5", "\xef\xa2\xa6", "\xef\xa2\xa7", "\xef\xa2\xa8", "\xef\xa2\xa9", "\xef\xa2\xaa", "\xef\xa2\xab", "\xef\xa2\xac", "\xef\xa2\xad", "\xef\xa2\xae", "\xef\xa2\xaf", "\xef\xa2\xb0", "\xef\xa2\xb1", "\xef\xa2\xb2", "\xef\xa2\xb3", "\xef\xa2\xb4", "\xef\xa2\xb5", "\xef\xa2\xb6", "\xef\xa2\xb7", "\xef\xa2\xb8", "\xef\xa2\xb9", "\xef\xa2\xba", "\xef\xa2\xbb", "\xef\xa2\xbc", "\xef\xa2\xbd", "\xef\xa2\xbe", "\xef\xa2\xbf", "\xef\xa3\x80", "\xef\xa3\x81", "\xef\xa3\x82", "\xef\xa3\x83", "\xef\xa3\x84", "\xef\xa3\x85", "\xef\xa3\x86", "\xef\xa3\x87", "\xef\xa3\x88", "\xef\xa3\x89", "\xef\xa3\x8a", "\xef\xa3\x8b", "\xef\xa3\x8c", "\xef\xa3\x8d", "\xef\xa3\x8e", "\xef\xa3\x8f", "\xef\xa3\x90", "\xef\xa3\x91", "\xef\xa3\x92", "\xef\xa3\x93", "\xef\xa3\x94", "\xef\xa3\x95", "\xef\xa3\x96", "\xef\xa3\x97", "\xef\xa3\x98", "\xef\xa3\x99", "\xef\xa3\x9a", "\xef\xa3\x9b", "\xef\xa3\x9c", "\xef\xa3\x9d", "\xef\xa3\x9e", "\xef\xa3\x9f", "\xef\xa3\xa0", "\xef\xa3\xa1", "\xef\xa3\xa2", "\xef\xa3\xa3", "\xef\xa3\xa4", "\xef\xa3\xa5", "\xef\xa3\xa6", "\xef\xa3\xa7", "\xef\xa3\xa8", "\xef\xa3\xa9", "\xef\xa3\xaa", "\xef\xa3\xab", "\xef\xa3\xac", "\xef\xa3\xad", "\xef\xa3\xae", "\xef\xa3\xaf", "\xef\xa3\xb0", "\xef\xa3\xb1", "\xef\xa3\xb2", "\xef\xa3\xb3", "\xef\xa3\xb4", "\xef\xa3\xb5", "\xef\xa3\xb6", "\xef\xa3\xb7", "\xef\xa3\xb8", "\xef\xa3\xb9", "\xef\xa3\xba", "\xef\xa3\xbb", "\xef\xa3\xbc", "\xef\xa3\xbd", "\xef\xa3\xbe", "\xef\xa3\xbf", "\xef\xbb\xbf",                 ' ',       '♪',      '♭',        '¼',        '½',        '⅓',        '⅔',        '⅕',        '⅖',        '⅗',        '⅘',        '⅙',        '⅚',        '⅛',        '⅜',        '⅝',        '¾',        '⅞',    'Ⓢ',        '|',       '?',        '$',      '!',      ';',          'à',        '·',      '¶',      '¯',       '«',      'ª',      '¨',      '§',        '¦',      '¥',         '¤',       '£',      '¢',       '¡',      '"',      '″',   '‘',       '`',      '°',      '¢',        '∞',        '¬',       '*',            ',',        '…',        '–',       '—',        '%',      '“',      '”',      '„',       '˝',      '•',  '’', chr(145), chr(146), chr(147), chr(148), chr(151), '&#8222;', '&#8220;', '&#146;',       '©',     '®',    'Ⓡ',     'ⓡ',       '™', '~\x{00a0}~siu',    "\r\n",      "\n", ' ');
            $str_replace_array = array( '&quest;',     '&#xBF;',   '&#xC0;',   '&#xC1;',   '&#xC2;',   '&#xC3;',   '&#xC4;',   '&#xC5;',   '&#xC6;',   '&#xC7;',   '&#xC8;',   '&#xC9;',   '&#xCA;',   '&#xCB;',   '&#xCC;',   '&#xCD;',   '&#xCE;',   '&#xCF;',   '&#xD0;',   '&#xD1;',   '&#xD2;',   '&#xD3;',   '&#xD4;',   '&#xD5;',   '&#xD6;',   '&#xD7;',   '&#xD8;',   '&#xD9;',   '&#xDA;',   '&#xDB;',   '&#xDC;',   '&#xDD;',   '&#xDE;',   '&#xDF;',   '&#xE0;',   '&#xE1;',   '&#xE2;',   '&#xE3;',   '&#xE4;',   '&#xE5;',   '&#xE6;',   '&#xE7;',   '&#xE8;',   '&#xE9;',   '&#xEA;',   '&#xEB;',   '&#xEC;',   '&#xED;',   '&#xEE;',   '&#xEF;',   '&#xF0;',   '&#xF1;',   '&#xF2;',   '&#xF3;',   '&#xF4;',   '&#xF5;',   '&#xF6;',   '&#xF7;',   '&#xF8;',   '&#xF9;',   '&#xFA;',   '&#xFB;',   '&#xFC;',   '&#xFD;',   '&#xFE;',   '&#xFF;',          '',             '',             '',          '',              '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',            '',              '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',             '',            '&nbsp;',  '&sung;', '&flat;', '&frac14;', '&frac12;', '&frac13;', '&frac23;', '&frac15;', '&frac25;', '&frac35;', '&frac45;', '&frac16;', '&frac56;', '&frac18;', '&frac38;', '&frac58;', '&frac34;', '&frac78;',  '&oS;', '&verbar;',       '?', '&dollar;', '&excl;',      ';',   '&agrave;', '&middot;', '&para;', '&macr;', '&laquo;', '&ordf;',  '&uml;', '&sect;', '&brvbar;',  '&yen;',  '&curren;', '&pound;', '&cent;', '&iexcl;', '&quot;', '&quot;',  '\'', '&grave;',  '&deg;', '&cent;',  '&infin;',    '&not;',   '&ast;',      '&comma;', '&hellip;',  '&ndash;', '&mdash;', '&percnt;', '&quot;', '&quot;', '&quot;',  '&quot;', '&bull;', '\'',      "'",      "'",      '"',      '"',      '-',       '"',       '"',      "'",  '&copy;', '&reg;', '&reg;', '&reg;', '&trade;',              '',   '<br/>',   '<br/>', ' ');
                // ============================================================
                // USE THIS INSTEAD TO DEBUG & LOOK FOR HIDDEN CHARACTERS
                // ============================================================
                // $str_find_array    = array('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9');
                // $str_replace_array = array( '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '');
                // ============================================================

            // ================================================================
            // STARTING LOOP
            // ================================================================
            foreach ($products["products"] as $product) {
                $product_id = $product['id'];
                $product_id_handle = $product['handle'];
                $product_title = trim(mb_convert_encoding(str_replace($str_find_array, $str_replace_array, strip_tags( $product['title'] ) ), 'UTF-8', mb_detect_encoding(strip_tags($product['title']))));

                // ============================================================
                // SET VAR to nothing then to retrieved data.
                // ============================================================
                $product_body_raw = '';
                $product_body_raw = $product['body_html'];
                // ============================================================
                // UPDATE TO STRIP NEW LINES (HAD TO FORCE REMOVE NEW LINES SINCE STR_REPLACE WILL NOT.)
                // ============================================================
                    $product_body_raw = preg_replace('/(\r\n|\r|\n)+/', '<br/>', $product_body_raw);
                // ============================================================
                // STRIP TAGS
                // ============================================================
                        $product_body_raw = strip_tags($product_body_raw);
                // ============================================================
                // UPDATE TO CLENSE THE DATA
                // ============================================================
                            $product_body_raw = str_replace($str_find_array, $str_replace_array, $product_body_raw);
                // ============================================================
                // THEN TRY TO CONVERT ENCODING
                // ============================================================
                                $product_body_raw = mb_convert_encoding($product_body_raw, 'UTF-8', mb_detect_encoding($product_body_raw));
                // ============================================================
                // THEN TRIM THE LINE & reset to destination var.
                // ============================================================
                                    $product_body_html = trim($product_body_raw);

                // ============================================================
                // SET VAR TO NOTHING THEN TO RETRIEVE THE DATA.
                // ============================================================
                $product_body_short_raw1 = '';
                $product_body_short_raw1 = $product['body_html'];
                // ============================================================
                // UPDATE TO STRIP NEW LINES (HAD TO FORCE REMOVE NEW LINES SINCE STR_REPLACE WILL NOT.)
                // ============================================================
                    $product_body_short_raw2 = '';
                    $product_body_short_raw2 = preg_replace('/(\r\n|\r|\n)+/', '<br/>', $product_body_short_raw1);
                // ============================================================
                // STRIP TAGS
                // ============================================================
                    $product_body_short_raw2 = strip_tags($product_body_short_raw2);
                // ============================================================
                // CLEAN LINE TO 140 CHARACTERS
                // LINE WILL BE LONGER IN RAW AS SYMBOLS WERE CONVERTED.
                // ============================================================
                        $product_body_short_raw3 = '';
                        $product_body_short_raw3 = substr($product_body_short_raw2,0,140);
                // ============================================================
                // UPDATE TO CLENSE THE DATA
                // ============================================================
                            $product_body_short_raw4 = '';
                            $product_body_short_raw4 = str_replace($str_find_array, $str_replace_array, $product_body_short_raw3 );
                // ============================================================
                // THEN TRY TO CONVERT ENCODING
                // ============================================================
                                $product_body_short_raw5 = '';
                                $product_body_short_raw5 = mb_convert_encoding($product_body_short_raw4, 'UTF-8', mb_detect_encoding($product_body_short_raw4));
                // ============================================================
                // THEN TRIM THE LINE & RESET TO DESTINATION VAR.
                // ============================================================
                                    $product_body_short_html = trim($product_body_short_raw5);
                // ============================================================
                // APPEND THE ELLIPSIES IF THE LENGTH IS > 140
                // ============================================================
                                        if (strlen($product_body_short_raw2) > 140) {$product_body_short_html = $product_body_short_html . '...';};

                $product_brand = trim(mb_convert_encoding(str_replace($str_find_array, $str_replace_array, strip_tags( $product['vendor'] ) ), 'UTF-8', mb_detect_encoding(strip_tags($product['vendor']))));
                $product_product_type = trim(mb_convert_encoding(str_replace($str_find_array, $str_replace_array, strip_tags( $product['product_type'] ) ), 'UTF-8', mb_detect_encoding(strip_tags($product['product_type']))));
                $product_google_category = $product['product_type'];
                $product_updated_at = trim(mb_convert_encoding(str_replace($str_find_array, $str_replace_array, strip_tags( $product['updated_at'] ) ), 'UTF-8', mb_detect_encoding(strip_tags($product['updated_at']))));
                $product_image = $product['image']['src'];
                $product_url = 'https://' . $shop_info['shop']['domain'] . '/products/' . $product['handle'];
                $product_keyword_tags = htmlspecialchars_decode(trim(mb_convert_encoding(str_replace($str_find_array, $str_replace_array, strip_tags( $product['tags'] ) ), 'UTF-8', mb_detect_encoding(strip_tags($product['tags'])))));

                foreach ($product['variants'] as $variant) {
                    $product_variant_id = $variant['id'];
                    $product_variant_title = trim(mb_convert_encoding(str_replace($str_find_array, $str_replace_array, strip_tags( $variant['title'] ) ), 'UTF-8', mb_detect_encoding(strip_tags($variant['title']))));
                    $product_variant_retail_price = mb_convert_encoding($variant['price'], 'UTF-8', mb_detect_encoding(strip_tags($variant['price'])));
                    $product_variant_sku = mb_convert_encoding($variant['sku'], 'UTF-8', mb_detect_encoding(strip_tags($variant['sku'])));
                    $product_variant_inventory_policy = mb_convert_encoding($variant['inventory_policy'], 'UTF-8', mb_detect_encoding(strip_tags($variant['inventory_policy'])));
                    $product_variant_sale_price = mb_convert_encoding($variant['compare_at_price'], 'UTF-8', mb_detect_encoding(strip_tags($variant['compare_at_price'])));
                    $product_variant_fulfillment_service = mb_convert_encoding($variant['fulfillment_service'], 'UTF-8', mb_detect_encoding(strip_tags($variant['fulfillment_service'])));
                    $product_variant_inventory_management = mb_convert_encoding($variant['inventory_management'], 'UTF-8', mb_detect_encoding(strip_tags($variant['inventory_management'])));
                    $product_variant_option1 = trim(mb_convert_encoding(str_replace($str_find_array, $str_replace_array, strip_tags( $variant['option1'] ) ), 'UTF-8', mb_detect_encoding(strip_tags($variant['option1']))));
                    $product_variant_option2 = trim(mb_convert_encoding(str_replace($str_find_array, $str_replace_array, strip_tags( $variant['option2'] ) ), 'UTF-8', mb_detect_encoding(strip_tags($variant['option2']))));
                    $product_variant_option3 =  trim(mb_convert_encoding(str_replace($str_find_array, $str_replace_array, strip_tags( $variant['option3'] ) ), 'UTF-8', mb_detect_encoding(strip_tags($variant['option3']))));
                    $product_variant_created_at = mb_convert_encoding($variant['created_at'], 'UTF-8', mb_detect_encoding(strip_tags($variant['created_at'])));
                    $product_variant_updated_at = mb_convert_encoding($variant['updated_at'], 'UTF-8', mb_detect_encoding(strip_tags($variant['updated_at'])));
                    $product_variant_taxable = mb_convert_encoding($variant['taxable'], 'UTF-8', mb_detect_encoding(strip_tags($variant['taxable'])));
                    $product_variant_barcode = mb_convert_encoding($variant['barcode'], 'UTF-8', mb_detect_encoding(strip_tags($variant['barcode'])));
                    $product_variant_grams = mb_convert_encoding($variant['grams'], 'UTF-8', mb_detect_encoding(strip_tags($variant['grams'])));
                    $product_variant_image_id = mb_convert_encoding($variant['image_id'], 'UTF-8', mb_detect_encoding($variant['image_id']));
                    $product_variant_inventory_quantity = mb_convert_encoding($variant['inventory_quantity'], 'UTF-8', mb_detect_encoding(strip_tags($variant['inventory_quantity'])));
                    $product_variant_weight = mb_convert_encoding($variant['weight'], 'UTF-8', mb_detect_encoding(strip_tags($variant['weight'])));
                    $product_variant_weight_unit = mb_convert_encoding($variant['weight_unit'], 'UTF-8', mb_detect_encoding(strip_tags($variant['weight_unit'])));
                    $product_variant_inventory_item_id = mb_convert_encoding($variant['inventory_item_id'], 'UTF-8', mb_detect_encoding(strip_tags($variant['inventory_item_id'])));
                    $product_variant_old_inventory_quantity = mb_convert_encoding($variant['old_inventory_quantity'], 'UTF-8', mb_detect_encoding(strip_tags($variant['old_inventory_quantity'])));
                    $product_variant_requires_shipping = mb_convert_encoding($variant['requires_shipping'], 'UTF-8', mb_detect_encoding(strip_tags($variant['requires_shipping'])));
                    $product_variant_image   = $product_image;
                    $product_variant_buy_url = $product_url . '?variant=' . $variant['id'];

                    foreach ($product['images'] as $image) {
                        if ($image['id'] === $product_variant_image_id) {
                            $product_variant_image = $image['src'];
                        }
                    }

                    $product_variant_large_image = preg_replace('#(\.[a-zA-Z]{3}\?)#', '_1024x1024$1', $product_variant_image);
                    $product_variant_medium_image = preg_replace('#(\.[a-zA-Z]{3}\?)#', '_300x300$1', $product_variant_image);
                    $product_variant_thumbnail_image = preg_replace('#(\.[a-zA-Z]{3}\?)#', '_100x100$1', $product_variant_image);

                    // ================================================================
                    // MAKEREQUEST - BUILD ARRAY
                    // DONT FORGET TO UPDATE THE HEADER ROW THAT TIES IN WITH THE ARRAY ORDER WRITTEN.
                    // ================================================================
                    $fields = array(
                        // PRODUCT VARIATION ID's
                            "\"" . $product_id_handle . "\",",
                            "\"" . $product_id . "\",",
                            "\"" . $product_variant_sku . "\",",
                            "\"" . $product_variant_barcode . "\",",
                            "\"" . $product_variant_id . "\",",
                            "\"" . $product_variant_inventory_item_id . "\",",

                            // ================================================
                            // PRODUCT INFO
                                // PRODUCT NAME
                                // PRODUCT TITLES
                            // ================================================
                            "\"" . $product_title . "\",",
                            "\"" . $product_variant_title . "\",",
                            // ================================================
                            // PRODUCT LONG DESCRIPTION
                            // ================================================
                            "\"" . $product_body_html . "\",",
                            // ================================================
                            // PRODUCT SHORT DESCRIPTION
                            // ================================================
                            "\"" . $product_body_short_html . "\",",
                            // PRODUCT VENDOR
                            "\"" . $product_brand . "\",",
                            "\"" . $product_product_type . "\",",// PRODUCT DEPARTMENT
                            "\"" . $product_google_category . "\",",// PRODUCT GOOGLE CATEGORY
                            "\"" . $product_keyword_tags . "\",", // PRODUCT KEYWORDS

                            // ================================================
                            // PRODUCT VARIANTS
                            // NOTE: PRODUCT RETAIL & SALE PRICE CAN FLIP
                            //       PER STORE - DEPENDS ON USER.
                            // ================================================
                            "\"" . $product_variant_retail_price . "\",",
                            "\"" . $product_variant_sale_price . "\",",
                            "\"" . $product_variant_buy_url . "\",",
                            "\"" . $product_variant_image_id . "\",",
                            "\"" . $product_variant_image . "\",",
                            "\"" . $product_variant_large_image . "\",",
                            "\"" . $product_variant_medium_image . "\",",
                            "\"" . $product_variant_thumbnail_image . "\",",
                            "\"" . $product_variant_option1 . "\",",
                            "\"" . $product_variant_option2 . "\",",
                            "\"" . $product_variant_option3 . "\",",

                            // ================================================
                            // PRODUCT VARIANT INVENTORY COUNTS
                            // ================================================
                            "\"" . $product_variant_inventory_quantity . "\",",
                            "\"" . $product_variant_old_inventory_quantity . "\",",

                            // ================================================
                            // PRODUCT VARIANT MEASUREMENTS
                            // ================================================
                            "\"" . $product_variant_grams . "\",",
                            "\"" . $product_variant_weight . "\",",
                            "\"" . $product_variant_weight_unit . "\",",
                            "\"" . $product_variant_requires_shipping . "\",",

                            // ================================================
                            // PRODUCT VARIANT MISC.
                            // ================================================
                            // "\"" . $product_variant_inventory_policy . "\",",
                            "\"" . $product_variant_fulfillment_service . "\",",
                            "\"" . $product_variant_inventory_management . "\"".PHP_EOL,
                            // "\"" . $product_variant_inventory_management . "\",",
                            // "\"" . $product_variant_taxable . "\",",
                            // "\"" . $product_variant_created_at . "\",",
                            // "\"" . $product_variant_updated_at . "\",",
                            // "\"" . $product_updated_at . "\"".PHP_EOL,
                    );

                    // ================================================================
                    // WRITE TO FILE
                    // ================================================================
                    foreach ($fields as $value) {
                        fwrite($file, $value);
                    }

                }
            }
        }

        print($argv[3] . ' ' .date("Ymd_H_i_s") . ": Finished Loop Thru Feed: " . $filename.PHP_EOL);

        // ====================================================================
        // CLOSE FILE HANDLE
        // ====================================================================
        fclose($file);

    }

    private function curlSetopts($ch, $method) {
        curl_setopt($ch, CURLOPT_HEADER, false);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
        curl_setopt($ch, CURLOPT_MAXREDIRS, 3);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, true);
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 2);
        curl_setopt($ch, CURLOPT_USERAGENT, 'shopify-php-api-client');
        curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 30);
        curl_setopt($ch, CURLOPT_TIMEOUT, 30);
        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, $method);
    }

    private function curlAppendQuery($url, $query) {
        if (empty($query)) {
            return $url;
        }

        if (is_array($query)) {
            return "$url?" . http_build_query($query);
        } else {
            return "$url?$query";
        }

    }

}

// ============================================================================
// PRINTS FIRST IN TERMINAL
// ============================================================================
// print($argv[3] . ' ' .date("Ymd_H_i_s") . ": \n\n");
// ============================================================================

class ShopifyCurlException extends Exception {}
class ShopifyApiException extends Exception {
    protected $method;
    protected $path;
    protected $params;
    protected $response_headers;
    protected $response;

    function __construct($method, $path, $params, $response_headers, $response) {
        $this->method = $method;
        $this->path = $path;
        $this->params = $params;
        $this->response_headers = $response_headers;
        $this->response = $response;

        parent::__construct($response_headers['http_status_message'], $response_headers['http_status_code']);
    }

    function getMethod() {return $this->method;}
    function getPath() {return $this->path;}
    function getParams() {return $this->params;}
    function getResponseHeaders() {return $this->response_headers;}
    function getResponse() {return $this->response;}
}

if (!isset($argv[4]) || trim($argv[4]) === '') {
    define('SHOPIFY_KEY', $argv[1]);
    define('SHOPIFY_PASSWORD', $argv[2]);
    define('SHOPIFY_STORE', $argv[3]);
} else {
    define('SHOPIFY_KEY', $argv[1]);
    define('SHOPIFY_PASSWORD', $argv[2]);
    define('SHOPIFY_STORE', $argv[3]);
    define('SHOPIFY_Collection', $argv[4]);}
;

if (!isset($argv[4]) || trim($argv[4]) === '') {
    print($argv[3] . ' ' .date("Ymd_H_i_s") . ": SHOPIFY_STORE Used:              " . $argv[3].PHP_EOL);
    print($argv[3] . ' ' .date("Ymd_H_i_s") . ": SHOPIFY_KEY Used:                " . $argv[1].PHP_EOL);
    print($argv[3] . ' ' .date("Ymd_H_i_s") . ": SHOPIFY_PASSWORD Used:           " . $argv[2].PHP_EOL);
} else {
    print($argv[3] . ' ' .date("Ymd_H_i_s") . ": SHOPIFY_STORE Used:              " . $argv[3].PHP_EOL);
    print($argv[3] . ' ' .date("Ymd_H_i_s") . ": SHOPIFY_KEY Used:                " . $argv[1].PHP_EOL);
    print($argv[3] . ' ' .date("Ymd_H_i_s") . ": SHOPIFY_PASSWORD Used:           " . $argv[2].PHP_EOL);
    print($argv[3] . ' ' .date("Ymd_H_i_s") . ": SHOPIFY_Collection Used:         " . $argv[4].PHP_EOL);
}
;

// ============================================================================
// print_r($argv);
// ============================================================================

$shopify = new Shopify(SHOPIFY_KEY, SHOPIFY_PASSWORD, SHOPIFY_STORE);
$shopify->getFeed(SHOPIFY_STORE . '.csv');

?>
