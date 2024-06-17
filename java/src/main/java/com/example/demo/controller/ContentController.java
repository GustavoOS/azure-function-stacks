package com.example.demo.controller;

import com.example.demo.model.Content;
import com.example.demo.model.ContentRepository;
import com.example.demo.view.ContentDTO;
import com.example.demo.view.ContentRequest;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/content")
@RequiredArgsConstructor
@Slf4j
public class ContentController {

  private final ContentRepository contentRepository;

  @GetMapping()
  public ResponseEntity<ContentDTO> getContent(@RequestParam(name = "id") Long id) {
    log.info("Getting content for id: " + id);
    var found = contentRepository.findById(id);
    return found.map(content -> ResponseEntity.ok(content.toDTO()))
        .orElseGet(() -> ResponseEntity.notFound().build());
  }

  @PostMapping()
  public ResponseEntity<ContentDTO> createContent(@RequestBody ContentRequest request) {
    log.info("Creating content");
    var content = new Content();
    content.setTitle(request.title());
    content.setColor(request.color());
    var dto = contentRepository.save(content).toDTO();
    return ResponseEntity.ok(dto);
  }

  @PutMapping
  public ResponseEntity<ContentDTO> updateContent(
      @RequestBody ContentRequest request,
      @RequestParam(name = "id") Long id) {
    log.info("Updating content");
    var contentOptional = contentRepository.findById(id);
    if (contentOptional.isEmpty()) {
      return ResponseEntity.notFound().build();
    }
    var content = contentOptional.get();
    content.setTitle(request.title());
    content.setColor(request.color());
    contentRepository.save(content);
    return ResponseEntity.ok(content.toDTO());
  }

  @DeleteMapping()
  public ResponseEntity<ContentDTO> deleteContent(@RequestParam(name = "id") Long id) {
    log.info("Deleting content");
    var contentOptional = contentRepository.findById(id);
    if (contentOptional.isEmpty()) {
      return ResponseEntity.notFound().build();
    }
    var content = contentOptional.get();
    contentRepository.delete(content);
    return ResponseEntity.ok(content.toDTO());
  }
}
