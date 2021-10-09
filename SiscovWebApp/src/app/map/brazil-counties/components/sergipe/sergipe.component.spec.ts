import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SergipeComponent } from './sergipe.component';

describe('SergipeComponent', () => {
  let component: SergipeComponent;
  let fixture: ComponentFixture<SergipeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SergipeComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SergipeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
