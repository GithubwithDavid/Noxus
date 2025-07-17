class VSCodeTypingAnimation {
    constructor(element, options = {}) {
        this.element = element;
        this.cursor = document.querySelector('.cursor');
        this.texts = options.texts || [
            "Hello, World!",
            "Welcome to coding!",
            "Build amazing things!",
            "Code with passion!",
            "Never stop learning!"
        ];
        
        this.typeSpeed = options.typeSpeed || 80;
        this.deleteSpeed = options.deleteSpeed || 25;
        this.pauseTime = options.pauseTime || 2000;
        this.deleteDelay = options.deleteDelay || 1500;
        
        this.currentTextIndex = 0;
        this.currentCharIndex = 0;
        this.isDeleting = false;
        this.isActive = false;
        
        this.init();
    }
    
    init() {
        this.element.innerHTML = '';
        setTimeout(() => this.animate(), 800);
    }
    
    animate() {
        if (this.isActive) return;
        
        this.isActive = true;
        const currentText = this.texts[this.currentTextIndex];
        
        // Manage cursor states
        if (!this.isDeleting && this.currentCharIndex < currentText.length) {
            // Typing state - animated cursor
            this.cursor.parentElement.classList.add('typing');
            this.cursor.parentElement.classList.remove('deleting');
        } else if (this.isDeleting) {
            // Deleting state - static cursor
            this.cursor.parentElement.classList.add('deleting');
            this.cursor.parentElement.classList.remove('typing');
        } else {
            // Idle state - normal animated cursor
            this.cursor.parentElement.classList.remove('typing', 'deleting');
        }
        
        if (!this.isDeleting) {
            // Typing phase
            if (this.currentCharIndex < currentText.length) {
                const char = currentText.charAt(this.currentCharIndex);
                const charSpan = document.createElement('span');
                
                // Handle spaces properly
                if (char === ' ') {
                    charSpan.innerHTML = '&nbsp;';
                } else {
                    charSpan.textContent = char;
                }
                
                charSpan.className = 'char';
                
                this.element.appendChild(charSpan);
                
                setTimeout(() => {
                    charSpan.style.animationDelay = '0s';
                }, 10);
                
                this.currentCharIndex++;
                
                const speed = this.typeSpeed + (Math.random() * 40 - 20);
                setTimeout(() => {
                    this.isActive = false;
                    this.animate();
                }, speed);
            } else {
                // Finished typing
                this.cursor.parentElement.classList.remove('typing');
                this.isActive = false;
                setTimeout(() => {
                    this.isDeleting = true;
                    this.animate();
                }, this.deleteDelay);
            }
        } else {
            // Deleting phase
            if (this.currentCharIndex > 0) {
                const chars = this.element.querySelectorAll('.char');
                const lastChar = chars[chars.length - 1];
                
                if (lastChar) {
                    lastChar.classList.add('char-delete');
                    
                    setTimeout(() => {
                        if (lastChar.parentNode) {
                            lastChar.parentNode.removeChild(lastChar);
                        }
                        this.currentCharIndex--;
                        
                        const speed = this.deleteSpeed + (Math.random() * 10 - 5);
                        setTimeout(() => {
                            this.isActive = false;
                            this.animate();
                        }, speed);
                    }, 80);
                } else {
                    this.currentCharIndex--;
                    setTimeout(() => {
                        this.isActive = false;
                        this.animate();
                    }, this.deleteSpeed);
                }
            } else {
                // Finished deleting - move to next text
                this.isDeleting = false;
                this.currentTextIndex = (this.currentTextIndex + 1) % this.texts.length;
                
                // Remove deleting state
                this.cursor.parentElement.classList.remove('deleting');
                
                setTimeout(() => {
                    this.isActive = false;
                    this.animate();
                }, this.pauseTime);
            }
        }
    }
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    const typedTextElement = document.getElementById('typed-text');
    
    // Smooth page entrance
    document.body.style.opacity = '0';
    document.body.style.transform = 'scale(0.95)';
    
    setTimeout(() => {
        document.body.style.transition = 'all 0.8s cubic-bezier(0.4, 0, 0.2, 1)';
        document.body.style.opacity = '1';
        document.body.style.transform = 'scale(1)';
    }, 100);
    
    new VSCodeTypingAnimation(typedTextElement, {
        texts: [
            "Hello, World!",
            "Welcome to coding!",
            "Build amazing things!",
            "Code with passion!",
            "Never stop learning!",
            "Keep exploring!",
            "Stay curious!",
            "Happy coding!"
        ],
        typeSpeed: 75,
        deleteSpeed: 20,
        pauseTime: 1800,
        deleteDelay: 1500
    });
});
