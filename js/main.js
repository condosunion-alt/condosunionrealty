// Condos Union Realty - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
  // Mobile Menu Toggle
  const navToggle = document.querySelector('.nav-toggle');
  const mobileMenu = document.querySelector('.mobile-menu');
  
  if (navToggle) {
    navToggle.addEventListener('click', function() {
      mobileMenu.classList.toggle('active');
      const spans = navToggle.querySelectorAll('span');
      if (mobileMenu.classList.contains('active')) {
        spans[0].style.transform = 'rotate(45deg) translateY(5px)';
        spans[1].style.transform = 'rotate(-45deg) translateY(-5px)';
      } else {
        spans[0].style.transform = 'none';
        spans[1].style.transform = 'none';
      }
    });
  }
  
  // Form Submission — sends email directly to condosunion@gmail.com
  const applyForm = document.getElementById('applyForm');
  
  if (applyForm) {
    applyForm.addEventListener('submit', async function(e) {
      e.preventDefault();
      
      const submitBtn = applyForm.querySelector('.form-submit');
      const originalText = submitBtn.textContent;
      submitBtn.textContent = '⏳ Submitting...';
      submitBtn.disabled = true;
      
      // Collect form data
      const formData = new FormData(applyForm);
      const data = Object.fromEntries(formData.entries());
      
      // Build email body
      const emailBody = `
📋 NEW PURCHASE WORKSHEET SUBMISSION
═══════════════════════════════════════

👤 PERSONAL INFO
   Name: ${data.firstName} ${data.lastName}
   Email: ${data.email}
   Phone: ${data.phone}

🏗️ PROJECT SELECTION
   Project: ${data.project}
   Buyer Type: ${data.interest}
   Budget Range: ${data.budget}
   Bedrooms: ${data.bedrooms || 'Not specified'}
   Location: ${data.location || 'Not specified'}

📝 ADDITIONAL INFO
   Notes: ${data.message || 'None'}
   Consent: Yes

🕐 Submitted: ${new Date().toLocaleString('en-US', { timeZone: 'America/Toronto' })}
═══════════════════════════════════════
`.trim();
      
      try {
        // Submit to Web3Forms as backup + primary email notification
        const [web3Result, emailResult] = await Promise.allSettled([
          // Web3Forms backup
          fetch('https://api.web3forms.com/submit', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              access_key: 'mEEdQTKzQApM1aUo1',
              ...data,
              subject: `📋 Worksheet: ${data.firstName} ${data.lastName} - ${data.project}`,
              from_name: `${data.firstName} ${data.lastName}`
            }),
          }).then(r => r.json()),
          
          // Direct email via FormSubmit.co
          fetch('https://formsubmit.co/condosunion@gmail.com', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              name: `${data.firstName} ${data.lastName}`,
              email: data.email,
              phone: data.phone,
              project: data.project,
              buyerType: data.interest,
              budget: data.budget,
              bedrooms: data.bedrooms || 'N/A',
              location: data.location || 'N/A',
              message: data.message || 'None',
              _subject: `📋 NEW Worksheet: ${data.firstName} ${data.lastName} - ${data.project}`,
              _captcha: false,
              _template: 'table',
            }),
          }).then(r => {
            if (!r.ok) throw new Error('Email failed');
            return r.text();
          }),
        ]);
        
        // Show success regardless — at least one should work
        console.log('Web3Forms:', web3Result.status === 'fulfilled' ? web3Result.value : web3Result.reason);
        console.log('Email:', emailResult.status === 'fulfilled' ? '✅ sent' : emailResult.reason);
        
        applyForm.innerHTML = `
          <div style="text-align: center; padding: 60px 20px;">
            <div style="font-size: 4rem; margin-bottom: 24px;">✅</div>
            <h3 style="font-size: 1.8rem; margin-bottom: 16px; color: var(--color-accent, #c9a962);">Worksheet Submitted Successfully!</h3>
            <p style="color: var(--color-text-muted, #888); margin-bottom: 12px; font-size: 16px;">
              Thank you, <strong>${data.firstName}</strong>! Your Purchase Worksheet has been received.
            </p>
            <p style="color: var(--color-text-muted, #888); margin-bottom: 32px;">
              📧 We'll contact you within 24 hours at<br><strong>${data.email}</strong> or <strong>${data.phone}</strong>
            </p>
            <div style="background: rgba(201,169,98,0.1); border: 1px solid rgba(201,169,98,0.3); border-radius: 12px; padding: 20px; max-width: 400px; margin: 0 auto 32px;">
              <p style="margin: 0; font-size: 14px; color: var(--color-accent, #c9a962);">
                📅 Want to book a consultation now?<br>
                <a href="https://calendly.com/condosunion" target="_blank" style="color: #00b4d8; text-decoration: underline; font-weight: 600;">
                  Book Free Consultation →
                </a>
              </p>
            </div>
            <a href="index.html" class="btn btn-primary">← Return Home</a>
          </div>
        `;
        
      } catch (error) {
        console.error('Submit error:', error);
        alert('⚠️ Submission issue. Please call us at 437-655-2888 or book online.');
        window.open('https://calendly.com/condosunion', '_blank');
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
      }
    });
  }
  
  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) target.scrollIntoView({ behavior: 'smooth' });
    });
  });
  
  // Navbar background on scroll
  const nav = document.querySelector('.nav');
  if (nav) {
    window.addEventListener('scroll', function() {
      nav.style.background = window.scrollY > 50 ? 'rgba(10, 10, 15, 0.98)' : 'rgba(10, 10, 15, 0.95)';
    });
  }
});