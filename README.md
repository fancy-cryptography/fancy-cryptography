# Fancy cryptography in the wild 🎩

Curated list of deployments of *fancy* cryptography.

A secondary goal of this list is to provide cryptographers with a list
of schemes that still need to be upgraded to post-quantum cryptography.

💫  [Contributions welcome](https://github.com/fancy-cryptography/fancy-cryptography/edit/main/README.md)

## Large-scale mainstream deployments

* **Signal private group system.**  
  Key-verification anonymous credentials.  
  Reading: [blog](https://signal.org/blog/signal-private-group-system/).
  Fully PQ: 😔.

* **Apple Homekit device enrollment**
  PAKE (SRP)
  Reading: [documentation](https://support.apple.com/nl-nl/guide/security/sec3a881ccb1/web)
	Fully PQ: 😔.

* **Apple Keychain key escrow**
  PAKE (SRP), threshold cryptography? ("majority of HSMs agrees")
  Reading: [documentation](https://support.apple.com/nl-nl/guide/security/sec3e341e75d/web)
  Fully PQ: 😔.

* **Apple Carkey**
  PAKE (SPAKE2+)
  [documentation](https://support.apple.com/nl-nl/guide/security/secf64471c16/web)
  Fully PQ: 😔.

* **Apple Private Relay.**  
  Blind signatures for anonymous tokens.  
  Reading: [overview](https://www.apple.com/icloud/docs/iCloud_Private_Relay_Overview_Dec2021.pdf).
  Fully PQ: 😔.

* **Apple Private Cloud Compute.**  
  Blind signatures for anonymous tokens.  
  Reading: [blog](https://security.apple.com/blog/private-cloud-compute/).
  Fully PQ: 😔.

* **WhatsApp encrypted backups.**  
  OPAQUE for backup key retrieval from PIN.  
  Reading: [presentation](https://iacr.org/submit/files/slides/2023/rwc/rwc2023/IT_2/slides.pdf),
           [Meta whitepaper](https://scontent-lhr8-1.xx.fbcdn.net/v/t39.8562-6/241394876_546674233234181_8907137889500301879_n.pdf?_nc_cat=108&ccb=1-7&_nc_sid=e280be&_nc_ohc=W2f98GDJW1MQ7kNvgEi9dJ0&_nc_ht=scontent-lhr8-1.xx&oh=00_AYC2S2KAHkBXa60RvLU1sOfP5Y_rCNgj_LOzHpSZ7RwStw&oe=666E0A26),
            [Academic paper](https://eprint.iacr.org/2023/843),
           [audit](https://research.nccgroup.com/wp-content/uploads/2021/10/NCC_Group_WhatsApp_E001000M_Report_2021-10-27_v1.2.pdf).
  Fully PQ: 😔.

* **Chrome compromised passwords check.**  
  Private Set Intersection.  
  Reading: [blog](https://security.googleblog.com/2019/12/better-password-protections-in-chrome.html).
  Fully PQ: 😔.

* **Cloudflare Geo Key Manager.**  
  Attribute/Identity-based encryption.  
  Reading: [blog](https://blog.cloudflare.com/inside-geo-key-manager-v2/).
  Fully PQ: 😔.
  
* (...)

## Web3 / Blockchain

* **ZCash**  
  Reading: TBD.
  Fully PQ: 😔.

* (...)
  
## Growing or niche

* **IACR voting**  
  Reading:  [Helios](https://www.usenix.org/legacy/events/sec08/tech/full_papers/adida/adida.pdf).
  Fully PQ: TBD.

* (...)

## See also

* [IETF PQUIP working group's "state of protocols and PQC"](https://github.com/ietf-wg-pquip/state-of-protocols-and-pqc)
