# Blink API Update Notes

## October 2025 Update

### Changes Made

Updated the APP_BUILD and DEFAULT_USER_AGENT constants to match the latest Blink Android app version (47.0, released August 2025).

**Previous values:**
- `APP_BUILD = "ANDROID_28373244"`  
- `DEFAULT_USER_AGENT = "27.0ANDROID_28373244"`

**Updated values:**
- `APP_BUILD = "ANDROID_30000192"`
- `DEFAULT_USER_AGENT = "47.0ANDROID_30000192"`

### Rationale

The Blink API servers check the User-Agent and APP-BUILD headers to verify that clients are using a supported version of the mobile app. Using outdated version identifiers can result in:

1. "App update required" messages (error code 105)
2. Rejected authentication attempts
3. Limited API functionality

### API Version Status

The library currently uses multiple API versions for different endpoints:
- **v5**: Account login (`/api/v5/account/login`)
- **v5**: Account operations (`/api/v5/accounts/...`)
- **v4**: Legacy account operations
- **v3**: Homescreen data
- **v2**: Video counts
- **v1**: Most camera and network operations

All API versions are currently functional and tests pass.

### Testing

All 174 unit tests pass with the updated constants:
- Authentication tests: ✓ 19/19 passed
- API tests: ✓ 19/19 passed
- Integration tests: ✓ 136/136 passed

### Future Considerations

1. **Monitor for App Updates**: The Blink Android app is updated regularly. Monitor APKMirror or similar sources for new versions.

2. **Build Number Pattern**: The build number appears to follow the pattern `ANDROID_<build_code>`. Future updates should maintain this format.

3. **Version Sync**: Keep the numeric version (e.g., "47.0") in sync with the APP_BUILD suffix.

4. **API Version Migration**: If Blink releases v6 or v7 API endpoints, test thoroughly before migration as they may have breaking changes.

### How to Update for Future Versions

When a new Blink Android app version is released:

1. Check APKMirror for the latest version details
2. Extract the versionCode from the APK metadata
3. Update constants in `blinkpy/helpers/constants.py`:
   ```python
   APP_BUILD = "ANDROID_<new_version_code>"
   DEFAULT_USER_AGENT = "<version>ANDROID_<new_version_code>"
   ```
4. Run full test suite: `pytest tests/`
5. Test with actual Blink hardware if possible

### References

- [Blink Home Monitor on APKMirror](https://www.apkmirror.com/apk/immedia-semiconductor/blink-home-monitor/)
- [GitHub Issue #855 - App Update Required](https://github.com/fronzbot/blinkpy/issues/855)
- [GitHub Issue #917 - PIN Code Rejection](https://github.com/fronzbot/blinkpy/issues/917)
