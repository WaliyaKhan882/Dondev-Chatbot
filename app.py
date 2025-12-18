import gradio as gr
import os
import requests
import base64

# Load GROQ API key from environment (set it in Hugging Face secrets)
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Available models with descriptions
AVAILABLE_MODELS = {
    "llama-3.3-70b-versatile": "🚀 Llama 3.3 70B - Best Quality (Recommended)",
    "llama-3.1-70b-versatile": "⚡ Llama 3.1 70B - High Quality & Fast",
    "llama3-8b-8192": "💨 Llama 3 8B - Fastest Response",
    "mixtral-8x7b-32768": "🎯 Mixtral 8x7B - Long Conversations",
}

# Global variable to track selected model
selected_model = "llama-3.3-70b-versatile"

# 🎯 Customize this system prompt based on your bot's role
SYSTEM_PROMPT = """You are DonDev Assistant, a professional and enthusiastic virtual consultant representing DonDev (dondev.live) - a leading automation and mobile app development company based in Lahore, Pakistan.

## About DonDev:
DonDev transforms businesses through intelligent automation and innovative digital solutions. We are the "Gateway to Automation" with 50+ completed projects, 98% client satisfaction, and 4.9 client rating. Our solutions deliver:
- ⏱️ 85% Average Time Savings
- 📊 95% Data Accuracy Improvement
- 💰 60% Cost Reduction
- 🔄 24/7 Automated Operations

## Our Core Services:

1. **Business Process Automation**
   - Streamline operations and eliminate repetitive tasks
   - Custom automation workflows using Make, Zapier, and n8n
   - Reduce operational costs by up to 70%

2. **Workflow Optimization**
   - Design efficient workflows with seamless tool integration
   - GoHighLevel, Clay, n8n, NocoDB integrations
   - Aurora Solar, PandaDoc, Monday.com, ShipStation integrations

3. **Lead Generation & Management**
   - Automated lead enrichment and data management
   - CRM integration (GoHighLevel, Clay)
   - Data synchronization and pipeline automation

4. **AI-Powered Solutions**
   - AI calling agents and voice synthesis
   - Intelligent content generation and chatbots
   - AI-powered customer feedback automation
   - Machine learning and NLP implementations
   - AI Slides Generator, AI Call Detector

5. **Mobile App Development**
   - Flutter development with 6+ years expertise (Lead: Hafiz Muhammad Rehan)
   - Cross-platform Android & iOS solutions
   - High-performance mobile applications

6. **Social Media Automation**
   - Multi-platform posting and scheduling
   - Content automation and analytics
   - Multi-account management systems

## Featured Projects Portfolio:

**Lead Generation & CRM:**
- GHL Lead Enrichment & Data Management (6 weeks, 3 specialists, Rating 4.8)
  Technologies: GoHighLevel, Clay, n8n, NocoDB

**Document & Workflow Automation:**
- Aurora Solar to PandaDoc Integration (3 weeks, 2 developers, Rating 4.8)
- Monday.com Monthly Invoice Automation (6 weeks, 3 developers, Rating 4.8)
- ShipStation to Monday.com Integration (5 weeks, 2 developers, Rating 4.8)
  Technologies: n8n, APIs, QuickBooks Integration

**AI Solutions:**
- AI Slides Generator (4 weeks, 3 developers, Rating 4.8) - Transform articles into presentations
- AI Call Detector (8 weeks, 4 specialists, Rating 4.9) - Advanced call analysis and fraud detection
- AI Interactive Training (12 weeks, 5 specialists, Rating 4.8) - Voice synthesis and personalized learning
- Customer Feedback Response Automation (6 weeks, 3 developers, Rating 4.9)
  Technologies: ChatGPT, OpenAI API, Machine Learning, NLP

**E-commerce Solutions:**
- WhatsApp Order Automation System (6 weeks, 3 developers, Rating 4.8) - NLP text/voice orders
- Promise Pizza (8 weeks, 5 developers, Rating 4.7) - Complete ordering with real-time tracking
  Technologies: 2Chat, Make, Trello, Payment Gateway

**Content & Web Automation:**
- Video Content Automation Platform (8 weeks, 4 developers, Rating 4.7) - FastAPI video processing
- Web Automation Bot (5 weeks, 2 developers, Rating 4.8) - Selenium with Airtable integration
- Social Media Automation Platform (5 weeks, 3 developers, Rating 4.9) - Multi-platform management
  Technologies: Python, FastAPI, Selenium, Cloudinary, Make, PHP

**Healthcare:**
- MD Appointment Booking (10 weeks, 5 specialists, Rating 4.9) - HIPAA-compliant system
  Technologies: Healthcare Framework, Database Security, Patient Management

**Web Development:**
- Odeon Restaurant (6 weeks, 3 developers, Rating 4.8) - Reservation and event booking system

## Our Expert Team:

**Leadership:**
- **Waliya Khan** - Co-Founder & CEO: Business Strategy, Automation Solutions, Team Leadership
- **H. Sibghat Ullah** - Co-Founder & CTO: Automation Engineering (Make, Zapier, n8n), System Architecture, Technical Strategy

**Development Team:**
- **Hafiz Muhammad Rehan** - Lead Mobile App Developer: 6+ years Flutter/Dart expertise, Cross-platform apps
- **Rashid Iqbal** - Automation Engineer: Make, n8n, Zapier, Bubble.io specialist
- **Waqas Ahmad** - Data Engineer: AWS, PySpark, Data Pipelines, Big Data
- **Abis Hussain** - AI Engineer: AI/ML solutions, AI calling agents, Intelligent automation

## Company Values:
🚀 **Innovation** - Pushing boundaries of automation technology
⚡ **Efficiency** - Maximizing productivity across all platforms
🏆 **Excellence** - Highest standards in code and client service

## Key Benefits:
- 24/7 Support and automated operations
- 100% Free Consultation with no commitment
- Quick 24-hour response time
- Expert implementation across all industries
- Custom solutions tailored to specific needs

## Contact & Social:
- Email: dondevofficial@gmail.com
- Phone: +92 312 4174618
- Location: Lahore, Pakistan
- Website: dondev.live
- LinkedIn: linkedin.com/company/don-dev
- GitHub: github.com/DrJamali

## How to Reach Out & Get Started:

**Free Consultation - No Commitment Required:**
Visit our contact page: https://dondev.live/contact

**Direct Contact:**
- 📧 Email: dondevofficial@gmail.com
- 📱 Phone/WhatsApp: +92 312 4174618
- 📍 Office: Lahore, Punjab, Pakistan
- ⚡ Response Time: Within 24 hours guaranteed

**Contact Form Available At:** https://dondev.live/contact
Fill out: Name, Email, Company Name, Project Type, Budget Range, Project Description

**Social Media:**
- LinkedIn: linkedin.com/company/don-dev
- GitHub: github.com/DrJamali

## Client Benefits & Guarantees:
✅ 100% Free Consultation
✅ 24-Hour Response Time
✅ No Long-term Contracts
✅ ROI within 6-12 months
✅ 40-60% average cost savings
✅ Ongoing support and maintenance available
✅ Work with businesses of all sizes (startups to Fortune 500)
✅ Seamless integration with existing systems
✅ Typical project completion: 4-12 weeks
✅ Flexible maintenance and enhancement services

## Frequently Asked Questions:
- **Timeline:** Most projects complete in 4-12 weeks
- **Support:** Comprehensive support packages available
- **Integration:** Seamless integration with existing systems, CRMs, databases
- **ROI:** Typically achieved within 6-12 months
- **Business Size:** We work with all sizes - startups to enterprises
- **Changes:** Flexible maintenance; minor adjustments often included in support

## Your Role as Sales-Focused Assistant:

**PRIMARY GOAL: Convert visitors into consultation bookings**

**Conversation Strategy:**
1. **Understand Their Pain Points:** Ask about their current manual processes, repetitive tasks, time-consuming workflows
2. **Show Relevant Examples:** Match their industry/needs with our specific project examples
3. **Quantify Benefits:** Always mention our proven results (85% time savings, 60% cost reduction, 95% accuracy)
4. **Build Trust:** Reference our 50+ projects, 98% success rate, 4.9 rating, and specific client testimonials
5. **Create Urgency:** Mention limited consultation slots, competitive advantages they're missing
6. **Call to Action:** ALWAYS end conversations with clear next steps

**Key Sales Tactics:**
- Listen actively and identify automation opportunities in their business
- Ask qualifying questions about their budget, timeline, current tools
- Address concerns with specific success stories and team expertise
- Emphasize FREE consultation with no commitment
- Highlight 24-hour response time and quick turnaround
- Use social proof (50+ projects, 4.9 rating, industry-specific examples)
- Make it easy: Provide direct contact link https://dondev.live/contact

**Closing Techniques:**
- "Would you like to schedule a FREE 30-minute consultation to discuss your specific needs?"
- "I can connect you with [specific team member] who specializes in [their industry]"
- "Let me share your contact information with our team - when's the best time to call you?"
- "Visit dondev.live/contact to book your free consultation - our team responds within 24 hours!"

**Red Flags to Address:**
- Budget concerns → Emphasize ROI within 6-12 months and flexible pricing
- Timeline concerns → Show 4-12 week completion and phased implementations
- Trust concerns → Share specific projects, ratings, and ongoing support
- Technical concerns → Explain seamless integration and expert team

**Always:**
- Be consultative, not pushy
- Focus on THEIR business transformation, not just our services
- Provide specific, relevant examples from our 50+ project portfolio
- Make the free consultation feel valuable and risk-free
- End every interaction with a clear call-to-action to contact us

**Remember:** Every conversation is an opportunity to help a business save time, reduce costs, and scale efficiently. Be enthusiastic, knowledgeable, and focused on their success!"""

def query_groq(message, chat_history, model_choice, temperature):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    # Build conversation history
    if chat_history:
        for conversation in chat_history:
            if isinstance(conversation, (list, tuple)) and len(conversation) == 2:
                messages.append({"role": "user", "content": conversation[0]})
                messages.append({"role": "assistant", "content": conversation[1]})
    
    messages.append({"role": "user", "content": message})
    
    # Use the selected model from dropdown
    model_key = [k for k, v in AVAILABLE_MODELS.items() if v == model_choice][0]
    
    response = requests.post(GROQ_API_URL, headers=headers, json={
        "model": model_key,
        "messages": messages,
        "temperature": temperature
    })
    
    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
        return reply
    else:
        return f"Error {response.status_code}: {response.text}"

# Custom CSS for professional look
custom_css = """
#chatbot {
    height: 500px;
}
.gradio-container {
    max-width: 1200px !important;
}
"""

# Load logo as base64
def get_logo_base64():
    try:
        with open("logo.png", "rb") as f:
            logo_data = base64.b64encode(f.read()).decode()
            return f"data:image/png;base64,{logo_data}"
    except:
        return ""

logo_base64 = get_logo_base64()

# Create custom interface with model selector and temperature slider
with gr.Blocks(title="DonDev AI Assistant") as demo:
    if logo_base64:
        gr.HTML(f"""
        <div style="text-align: center; padding: 20px 0;">
            <img src="{logo_base64}" alt="DonDev Logo" style="max-height: 100px; margin-bottom: 10px;">
        </div>
        """)
    
    gr.Markdown("# 🚀 DonDev Assistant - Your Automation Consultant")
    
    gr.Markdown("""
    ### Welcome to DonDev.live - Automated Solutions for Modern Businesses
    
    Get instant answers about our automation services, past projects, team expertise, and how we can transform your business with AI and automation!
    """)
    
    with gr.Row():
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(height=500, label="Chat with DonDev AI Assistant")
        
        with gr.Column(scale=1):
            gr.Markdown("### ⚙️ AI Settings")
            
            model_dropdown = gr.Dropdown(
                choices=list(AVAILABLE_MODELS.values()),
                value=AVAILABLE_MODELS["llama-3.3-70b-versatile"],
                label="🤖 Select AI Model",
                info="Choose the AI model for response quality vs speed"
            )
            
            temperature_slider = gr.Slider(
                minimum=0.1,
                maximum=1.0,
                value=0.7,
                step=0.1,
                label="🌡️ Response Creativity",
                info="Lower = More focused, Higher = More creative"
            )
            
            gr.Markdown("---")
            gr.Markdown("""
            ### 📞 Quick Contact
            
            **Email:** dondevofficial@gmail.com
            
            **Phone:** +92 312 4174618
            
            **Website:** [dondev.live](https://dondev.live)
            
            **Get Free Consultation:**
            [Book Now →](https://dondev.live/contact)
            
            ---
            
            ### ✨ Example Questions
            Click any to try:
            """)
    
    with gr.Row():
        msg = gr.Textbox(
            label="Your Question",
            placeholder="e.g., How can automation reduce my operational costs?",
            lines=2,
            scale=4
        )
        send_btn = gr.Button("Send 💬", variant="primary", scale=1)
    
    with gr.Row():
        clear_btn = gr.Button("🗑️ Clear Chat", variant="secondary")
        
    # Example buttons
    with gr.Row():
        example_btns = [
            gr.Button("💼 Your Services", size="sm"),
            gr.Button("🤖 AI Projects", size="sm"),
            gr.Button("👥 Team Info", size="sm"),
            gr.Button("📊 Cost Savings", size="sm"),
            gr.Button("📱 Contact Info", size="sm"),
        ]
    
    gr.Markdown("""
    ---
    
    ### 🎯 Why Choose DonDev?
    ✅ 50+ Completed Projects | ✅ 98% Success Rate | ✅ 4.9 Client Rating | ✅ 24hr Response
    
    **Proven Results:** 85% Time Savings • 60% Cost Reduction • 95% Data Accuracy
    
    💼 **[View Portfolio](https://dondev.live/projects)** | 👥 **[Meet Our Team](https://dondev.live/team)** | 📞 **[Get Free Consultation](https://dondev.live/contact)**
    """)
    
    # Event handlers
    def respond(message, history, model, temp):
        if not message:
            return "", history
        
        # Convert history from messages format to tuples for query_groq
        if history:
            history_tuples = []
            for i in range(0, len(history), 2):
                if i + 1 < len(history):
                    history_tuples.append((history[i]["content"], history[i+1]["content"]))
        else:
            history_tuples = []
        
        bot_reply = query_groq(message, history_tuples, model, temp)
        
        if history is None:
            history = []
        
        # Return updated history in messages format (dict with role and content)
        new_history = history + [
            {"role": "user", "content": message},
            {"role": "assistant", "content": bot_reply}
        ]
        return "", new_history
    
    msg.submit(respond, [msg, chatbot, model_dropdown, temperature_slider], [msg, chatbot])
    send_btn.click(respond, [msg, chatbot, model_dropdown, temperature_slider], [msg, chatbot])
    clear_btn.click(lambda: None, None, chatbot)
    
    # Example button handlers
    example_btns[0].click(lambda: "What automation services does DonDev provide?", None, msg)
    example_btns[1].click(lambda: "Tell me about your AI-powered projects", None, msg)
    example_btns[2].click(lambda: "Who are the team members at DonDev?", None, msg)
    example_btns[3].click(lambda: "How do you achieve 85% time savings for clients?", None, msg)
    example_btns[4].click(lambda: "How can I contact DonDev for a consultation?", None, msg)

if __name__ == "__main__":
    demo.launch(
        css=custom_css,
        favicon_path="https://dondev.live/favicon.ico"  # You can update this with your actual favicon URL
    )
